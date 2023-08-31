from src import (
    construct_bar,
)

from src.user_inputs import InputController
from src.spotify import spotify_service
from src.data_service import data_service
from dotenv import load_dotenv

load_dotenv()


def main():
    """Runs database creation command and allows user-specified response to generate requested graph."""
    input_controller = InputController(data_service, spotify_service)
    input_controller.check_for_data_refresh()

    requests_dict = {"s": "short_term", "m": "medium_term", "l": "long_term"}
    request_input_list = input_controller.get_sml_request()
    output_terms = [requests_dict[input_item] for input_item in request_input_list]

    bar = construct_bar(*output_terms)

    input_controller.get_save_show_request(bar)


if __name__ == "__main__":
    main()
