from Utilities import SelectionValidation as sv

WELCOME_MESG = "Please select the dataset to analyse (A Training/ B Test):"
MODULE_DICT = {"A": "TrainingSetAnalysis", "B": "TestSetAnalysis"}

input_validation = sv.SelectionValidation(selection_dict=MODULE_DICT,
                                          menu_message="",
                                          welcome_message=WELCOME_MESG)
function_select = input_validation.validation()

exec("from Analysis import " + MODULE_DICT[function_select])
