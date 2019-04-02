import sys
import importlib
import SelectionValidation as sv

MENU_MESG = "========================================\n" \
               "MENU\n" \
               "1  Data Analysis\n" \
               "2  Model Training\n" \
               "3  Result Evaluation\n" \
               "4  Demonstration\n" \
               "5  EXIT\n" \
               "========================================"

PACKAGE_DICT = {"1": "Analysis",
                "2": "ModelsTraining",
                "3": "Evaluation",
                "4": "ModelsTraining",
                "5": "EXIT"}

WELCOME_MESG = "Please select the function of the application:"

input_validation = sv.SelectionValidation(selection_dict=PACKAGE_DICT,
                                          menu_message=MENU_MESG,
                                          welcome_message=WELCOME_MESG)
user_select = input_validation.validation()

if user_select == "5":
    sys.exit(0)

del input_validation

print("Executing" + " \"" + PACKAGE_DICT[user_select] + "\" module.")

importlib.import_module(PACKAGE_DICT[user_select])

print("Module \"" + PACKAGE_DICT[user_select] + "\" is finished.")
