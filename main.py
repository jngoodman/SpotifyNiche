from src.__init__ import Bar, get_dataframes, INPUT_REQUEST_KEYS


def main():
    request_key = input("What time range would you like to view? (S/M/L/All): ").lower()
    key = INPUT_REQUEST_KEYS[request_key]
    bar = Bar(dataframe_dict=get_dataframes(), key=key)
    bar.construct_bar()
    bar.add_elements()
    bar.show_bar()


if __name__ == "__main__":
    main()
