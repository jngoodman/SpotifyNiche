from dotenv import load_dotenv
from os import getenv
from src import (
    construct_bar,
)

from src.user_inputs import InputController
from src.spotify import create_spotify_service
from src.data_service import DataService
from src.database import Database
from src.constants import SQL_DATA

load_dotenv()

client_id = getenv("CLIENT_ID")
client_secret = getenv("CLIENT_SECRET")
redirect_uri = getenv("REDIRECT_URI")


def main():
    """Runs database creation command and allows user-specified response to generate requested graph."""
    data_service = DataService(Database(SQL_DATA, print=True))
    input_controller = InputController(
        data_service,
        create_spotify_service(
            client_id,
            client_secret,
            redirect_uri,
        ),
    )
    input_controller.check_for_data_refresh()

    requests_dict = {"s": "short_term", "m": "medium_term", "l": "long_term"}
    request_input_list = input_controller.get_sml_request()
    output_terms = [requests_dict[input_item] for input_item in request_input_list]

    bar = construct_bar(*output_terms)

    input_controller.get_save_show_request(bar)


if __name__ == "__main__":
    main()
