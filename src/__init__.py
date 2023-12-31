from src.constants import TERMS, GRAPH, TEXT
from src.handle_raw_data import GetRawData, ConvertRawData
from src.handle_display_data import BarElements, FlavourText, Bar
from src.handle_sql_data import Connection, create_db, retrieve_from_db
from src.user_inputs import get_sml_request, check_for_new_database, get_save_show_request, convert_user_inputs


def construct_bar(*args: str):
    bar = Bar(*args)
    bar.extract_data()
    bar.construct_bars()
    bar.determine_title_suffix()
    bar.adjust_axes()
    bar.adjust_labels()
    bar.add_elements()
    return bar
