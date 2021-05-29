import re
from os import listdir
from os.path import isfile, join, splitext


# RegEx patten to match copied files: "'file_name' (digit)"
copy_pattern = re.compile(r'^(?:(?! \(\d\)$).)*')


def get_files_list(files_path: str):
    """
    Returns a list of file names from the directory
    """
    return [splitext(f)[0] for f in listdir(files_path) if isfile(join(files_path, f))]

def count_spaces(string: str):
    """
    Counts the number of spaces in the string\n
    :return: int - number of spaces
    """
    counter = 0
    for sym in string:
        if sym == ' ':
            counter += 1
    return counter


def replace_spaces_by_matches_count(string: str, matches_count: int):
    """
    Replace matches_count spaces from left to right\n
    :return: string - with replaced spaces
    """
    if matches_count == -1:
        return string

    sym_list = list(string)
    result = ''

    for index, item in enumerate(sym_list):
        if matches_count == 0:
            break
        if item == ' ':
            sym_list[index] = '_'
            matches_count -= 1
    return result.join(sym_list)


def normalize_name(name: str):
    """
    Removes all spaces except last one before (digit).\n
    E.g. test string (1) => test_string (1)
    :return: string - normalized string
    """
    if name == re.findall(copy_pattern, name)[0]:
        spaces = count_spaces(name)
    else:
        spaces = count_spaces(name) - 1
    return replace_spaces_by_matches_count(name, spaces)


def remove_copy_mark(file_name: str):
    """
    Normalizes string and removes ' (digit)' part of the string. Used to remove parts added to duplicates\n
    E.g. test string (1) => test_string
    :return: string - without ' (digit)'
    """
    file_name = normalize_name(file_name)
    exclude_words = ['image']
    for exclude_word in exclude_words:
        if re.sub(copy_pattern, '', file_name).find(exclude_word) == -1:
            return file_name.split()[0]
        else:
            return file_name


def print_dict_keys(dict_object: dict):
    """
    debug method
    """
    for key in dict_object:
        print(key + ": " + str(dict_object[key]))


def main():
    pass


if __name__ == "__main__":
    main()