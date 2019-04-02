import pandas as pd


def get_dataframe(directory, filename):
    return csv_open(directory, filename)


class csv_open:

    """This class helps converts csv file into pandas dataframe."""

    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def __enter__(self):
        return pd.read_csv(self.directory + self.filename)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type:", exc_type)
        print("value:", exc_val)
        print("trace:", exc_tb)
