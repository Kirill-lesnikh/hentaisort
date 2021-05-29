from modules import formatter
import re


def get_duplicates_dict(files_list: list):
    """
    Generates dictionary {file name: [duplicate name 1, duplicate name 2]}\n
    (image|file etc.) - excluded file names\n
    :return: dict
    """
    duplicates_dict = {}
    for file in files_list:
        if re.search(r'^.* \(\d\)$', file) and not re.search(r'^(image|file|image0|image1) \(\d\)$', file):
            try:
                duplicates_dict[formatter.remove_copy_mark(file)]
            except KeyError:
                duplicates_dict[formatter.remove_copy_mark(file)] = []
            duplicates_dict[formatter.remove_copy_mark(file)].append(file)
    return duplicates_dict


def main():
    fornatter.print_dict_keys(get_duplicates_dict(files))


if __name__ == "__main__":
    main()
