from .handle_raw_data import GetRawData, ConvertRawData
from .graph import BarElements, FlavourText, Bar
from .database import Database, create_db, retrieve_from_db
from .user_inputs import (
    get_sml_request,
    check_for_new_database,
    get_save_show_request,
)


def construct_bar(*args: str):
    bar = Bar(*args)
    bar.extract_data()
    bar.construct_bars()
    bar.determine_title_suffix()
    bar.adjust_axes()
    bar.adjust_labels()
    bar.add_elements()
    return bar
