import pandas as pd


def get_dataframe(directory, filename):
    return CSVOpen(directory, filename)


class CSVOpen:

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
