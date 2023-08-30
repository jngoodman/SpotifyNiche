from .handle_raw_data import GetRawData, ConvertRawData
from .graph import BarElements, FlavourText, Bar
from .database import Database, create_db, retrieve_from_db
from .user_inputs import (
    get_sml_request,
    check_for_new_database,
    get_save_show_request,
)
from .constants import SQL_DATA
from .data_service.service import DataService
from .data_service import data_service


def construct_bar(*args: str):
    terms = [*args]
    means = dict(
        (result.term, result.popularity)
        for result in data_service.get_average_popular_artists_by_term()
    )
    data = data_service.get_all_artists_for_terms(terms)

    bar = Bar(terms, means, data)
    bar.construct_bars()
    bar.determine_title_suffix()
    bar.adjust_axes()
    bar.adjust_labels()
    bar.add_elements()
    return bar
