class DatasetDirectory:

    def __init__(self):

        # Default value
        dataset_dir_default = "E:\\Developing\\TrainingSet\\"
        train_dir_default = "E:\\Developing\\TrainingSet\\train_v2\\"
        test_dir_default = "E:\\Developing\\TrainingSet\\test_v2\\"
        csv_label_default = "TrainingSetAnalysis.csv"

        ATTR_NAME = ["dataset directory", "training set directory", "test set directory", "CSV labelling file name"]

        self.dataset_dir = self.set_up_value(dataset_dir_default, ATTR_NAME[0])
        print(self.dataset_dir)
        self.train_dir = self.set_up_value(train_dir_default, ATTR_NAME[1])
        print(self.train_dir)
        self.test_dir = self.set_up_value(test_dir_default, ATTR_NAME[2])
        print(self.test_dir)
        self.csv_label = self.set_up_value(csv_label_default, ATTR_NAME[3])
        print(self.csv_label)

    def set_up_value(self, default_value, value_name):
        input_value = input("Please type in " + value_name +
                            ":\n(Type nothing will use default value:\"" + default_value + "\")")

        if input_value == '':
            return default_value
        else:
            return input_value
