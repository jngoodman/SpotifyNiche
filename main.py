from src.__init__ import construct_bar, get_sml_request, check_for_new_database, get_save_show_request


def main():
    """Runs database creation command and allows user-specified response to generate requested graph."""
    check_for_new_database()
    requests_dict = {
        's': 'short_term',
        'm': 'medium_term',
        'l': 'long_term'
    }
    request_input_list = get_sml_request()
    request_output_list = []
    for key, value in requests_dict.items():
        if key in request_input_list:
            request_output_list.append(value)
    bar = construct_bar(*request_output_list)
    get_save_show_request(bar)


if __name__ == "__main__":
    main()
