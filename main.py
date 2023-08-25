from src.__init__ import construct_bar, create_db


def main():
    create_db()
    requests_dict = {
        's': 'short_term',
        'm': 'medium_term',
        'l': 'long_term'
    }
    insert_request = input("What would you like to insert? Any combination of (s/m/l): ").lower()
    request_input_list = [request for request in insert_request]
    request_output_list = []
    for key, value in requests_dict.items():
        if key in request_input_list:
            request_output_list.append(value)
    construct_bar(*request_output_list)


if __name__ == "__main__":
    main()
