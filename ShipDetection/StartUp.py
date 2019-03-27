import sys
import importlib

menu_message = "========================================\n" \
               "MENU\n" \
               "1  Data Analysis\n" \
               "2  Data Augmentation and Pre-processing\n" \
               "3  Model Training\n" \
               "4  Result Evaluation\n" \
               "5  Demonstration\n" \
               "6  EXIT\n" \
               "========================================"

print("Final Year Project Version 1.0.1")
print(menu_message)

user_select = input("Please input the function of the script:")

PACKAGE_DICT = {"1": "Analysis",
                "2": "DataPrep",
                "3": "ModelTraining",
                "4": "Evaluation",
                "5": "Models",
                "6": "EXIT"}

# Count the times of wrong input, pop up menu again when > 5
wrong_input_counter = 0

while user_select not in PACKAGE_DICT:
    if wrong_input_counter > 5:
        print(menu_message)
        wrong_input_counter = 0
        user_select = input("Please input the function of the script:")
        continue
    user_select = input("Invalid selection, please select again:")
    wrong_input_counter += 1


if user_select == "6":
    sys.exit(0)


print("Executing" + " \"" + PACKAGE_DICT[user_select] + "\" module.")

importlib.import_module(PACKAGE_DICT[user_select])

print("Module \"" + PACKAGE_DICT[user_select] + "\" is finished.")
