import sys
import importlib
from Utilities import SelectionValidation as sv
from Utilities import DatasetDirectory as dsd
import GlobalVariable as gv


MENU_MESG = "========================================\r\n" \
            "MENU\r\n" \
            "1  Data Analysis\r\n" \
            "2  Model Training\r\n" \
            "3  Result Evaluation\r\n" \
            "4  EXIT\r\n" \
            "========================================\r\n"

PACKAGE_DICT = {"1": "Analysis",
                "2": "ModelsTraining",
                "3": "Evaluation",
                "4": "EXIT"}

WELCOME_MESG = "Please select the function of the application:"

input_validation = sv.SelectionValidation(selection_dict=PACKAGE_DICT,
                                          menu_message=MENU_MESG,
                                          welcome_message=WELCOME_MESG)
user_select = input_validation.validation()

if user_select == "1" or user_select == "2":
    gv.project_dir = dsd.DatasetDirectory()

if user_select == "4":
    sys.exit(0)

del input_validation

print("Executing" + " \"" + PACKAGE_DICT[user_select] + "\" module.")

importlib.import_module(PACKAGE_DICT[user_select])

print("Module \"" + PACKAGE_DICT[user_select] + "\" is finished.")

