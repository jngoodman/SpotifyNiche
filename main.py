from src import construct_bar, convert_user_inputs, check_for_new_database, get_save_show_request


def main():
    """Runs database creation command and allows user-specified response to generate requested graph."""
    check_for_new_database()
    request_output_list = convert_user_inputs()
    bar = construct_bar(*request_output_list)
    get_save_show_request(bar)


if __name__ == "__main__":
    main()
