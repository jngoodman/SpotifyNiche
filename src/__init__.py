from src.constants.__init__ import TERMS, GRAPH, TEXT, CREATE_DATA_STRUCTURE, INSERT_VALUES_INTO_TABLE, EXTRACT_VALUES
from src.extract_data_from_spotify.__init__ import APICall, GetArtistData
from src.handle_display_data.__init__ import BarElements, FlavourText, Bar
from src.handle_sql_data.__init__ import Connection, create_db, retrieve_from_db


def construct_bar(*args: str):
    bar = Bar(*args)
    bar.extract_data()
    bar.construct_bars()
    bar.determine_title_suffix()
    bar.adjust_axes()
    bar.adjust_labels()
    bar.add_elements()
    bar.show_bar()
