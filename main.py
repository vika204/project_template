from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import print_to_console, write_to_file_builtin

def main():
    text1 = read_from_console()
    text2 = read_from_file_builtin()
    text3 = read_from_file_pandas()

    print_to_console(text1)
    print_to_console(text2)
    print_to_console(text3)

    write_to_file_builtin(f"{text1}\n{text2}\n{text3}")

if __name__ == "__main__":
    main()