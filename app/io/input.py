import pandas as pd

def read_from_console():
    """Reads text input from the console."""
    return input("Enter text: ")

def read_from_file_builtin():
    """Reads text from a file using Python's built-in capabilities."""
    with open("data/input.txt", "r") as file:
        return file.read()

def read_from_file_pandas():
    """Reads data from a file using pandas library."""
    return pd.read_csv("data/input.csv").to_string()