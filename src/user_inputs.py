from os import path, remove
from src.handle_raw_data.__init__ import GetRawData, ConvertRawData
from src.constants.__init__ import SQL_DATA
from src.handle_sql_data.__init__ import create_db


def get_new_database():
    request_instance = GetRawData()
    request_instance.make_request()
    request_instance.get_raw_data_from_request()
    sql_ready_data = ConvertRawData(request_instance.raw_data).return_rows()
    create_db(sql_ready_data)


def check_for_new_database():
    """Asks the user if they'd like to replace an existing database if one exists. Else, automatically creates one."""
    if path.isfile(SQL_DATA):
        request_accepted = False
        while not request_accepted:
            get_update = input("Local data found. Would you like to update 'database.db' from Spotify? (Y/N): ").lower()
            if get_update == 'y':
                remove(SQL_DATA)
                print("Old database deleted. Requesting new database...")
                get_new_database()
                request_accepted=True
            elif get_update == 'n':
                print("Using existing database...")
                request_accepted = True
            else:
                print("Invalid response.")
    else:
        print("No local data found. Requesting data from Spotify.")
        get_new_database()


def get_sml_request():
    """Gets user request for what terms they would like to insert. Accepts only a combination of 'sml'."""
    insert_request: str = ''
    request_accepted = False
    while not request_accepted:
        insert_request = input("What would you like to view? Any combination of (s/m/l): ").lower()
        fail_list = []
        for letter in insert_request:
            if letter not in 'sml':
                fail_list.append(letter)
            if not fail_list:
                request_accepted = True
    return [request for request in insert_request]
