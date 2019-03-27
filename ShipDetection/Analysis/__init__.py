
'''
# Debug: package step-in indicator
print(__name__)
'''

'''
data_set_dir = input("Please input the directory of dataset:")

training_set_postfix = "train_v2"
test_set_postfix = "test_v2"

print(data_set_dir + training_set_postfix)
print(data_set_dir + test_set_postfix)
'''

function_select = input("Please select the dataset to analyse (A Training/ B Test):")
MODULE_DICT = {"A": "TrainingSetAnalysis", "B": "TestSetAnalysis"}

while function_select not in MODULE_DICT:
    input("Invalid input, please input again(A for Training / B for Test):")


exec("from Analysis import " + MODULE_DICT[function_select])

