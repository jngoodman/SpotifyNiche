from src.__init__ import construct_bar, create_db
from os import path, remove


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


def ask_to_update():
    """Asks the user if they'd like to replace an existing database if one exists."""
    if path.isfile('database.db'):
        request_accepted = False
        while not request_accepted:
            ask_to_update = input("Would you like to request an updated 'database.db' from Spotify? (Y/N): ").lower()
            if ask_to_update == 'y':
                remove('database.db')
                print("Old database deleted. Requesting new database...")
                request_accepted = True
            elif ask_to_update == 'n':
                print("Using existing database...")
                request_accepted = True
            else:
                print("Invalid response.")


def main():
    """Runs database creation command and allows user-specified response to generate requested graph."""
    ask_to_update()
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
