def print_to_console(text):
    """Prints text to the console."""
    print(text)

def write_to_file_builtin(text):
    """Writes text to a file using Python's built-in capabilities."""
    with open("data/output.txt", "w") as file:
        file.write(text)