from src.__init__ import construct_bar, create_db


def get_user_request():
    """Gets user request for what terms they would like to insert. Accepts only a combination of 'sml'."""
    insert_request: str = ''
    request_accepted = False
    while not request_accepted:
        insert_request = input("What would you like to insert? Any combination of (s/m/l): ").lower()
        fail_list = []
        for letter in insert_request:
            if letter not in 'sml':
                fail_list.append(letter)
            if not fail_list:
                request_accepted = True
    return [request for request in insert_request]


def main():
    """Runs database creation command and allows user-specified response to generate requested graph."""
    create_db()
    requests_dict = {
        's': 'short_term',
        'm': 'medium_term',
        'l': 'long_term'
    }
    request_input_list = get_user_request()
    request_output_list = []
    for key, value in requests_dict.items():
        if key in request_input_list:
            request_output_list.append(value)
    construct_bar(*request_output_list)


if __name__ == "__main__":
    main()
