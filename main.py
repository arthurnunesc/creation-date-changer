from subprocess import call


def main():
    file_path = "/Users/anunes-c/Desktop/MyFile.txt"
    desired_date = "01/01/2022 01:14:25"
    file_name_1 = ""
    file_name_2 = ""
    file_name_3 = ""
    change_file_creation_date(file_path, desired_date)


def change_file_creation_date(file_path, desired_date):
    # command = 'SetFile -d "{}" {}'.format(strftime("%m/%d/%Y %H:%M:%S"), file_path)
    command = f"SetFile -d '{desired_date}' {file_path}"
    call(command, shell=True)


if __name__ == "__main__":
    main()
