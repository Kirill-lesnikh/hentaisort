from modules import duplicates_checker as dch


# General config:
# main_path = 'Z:\\usb\\USB\\[_Art]'
main_path = 'Z:\\usb\\USB\\[_Art]\\0test'
files = dch.formatter.get_files_list(main_path)


def main():
    dch.formatter.print_dict_keys(dch.get_duplicates_dict(files))


if __name__ == "__main__":
    main()
