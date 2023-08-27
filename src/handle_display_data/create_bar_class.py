from matplotlib import pyplot as plt
from src.constants.__init__ import GRAPH, EXTRACT_VALUES
from src.handle_sql_data.__init__ import retrieve_from_db
from src.handle_display_data.flavour_text import FlavourText
from src.handle_display_data.graph_elements import BarElements


class Bar:

    def __init__(self, *args):
        """Accepts 'short_term', 'medium_term' and 'long_term' as appropriate *args."""
        self.terms: list = [*args]
        self.data = None

    def extract_data(self):
        """Creates an ad-hoc SQLite command to allow data from the database to be recovered in a pandas format
        based on the terms requested in *args"""
        extraction_list = []
        counter = 1
        for term in self.terms:
            extraction_list.append(f"term IS '{term}'")
            if counter < len(self.terms):
                extraction_list.append("OR")
            counter += 1
        extraction_string = ' '.join(extraction_list)
        sql_command = f"""{EXTRACT_VALUES.VALUES_INTRO} {extraction_string} {EXTRACT_VALUES.VALUES_OUTRO}"""
        self.data = retrieve_from_db(sql_command, pandas=True)

    def construct_bars(self):
        """Generates pyplot figure. Plots popularity data on to its range to force inclusion of duplicates, then
        substitutes range for the artist_name values."""
        data_range = range(len(self.data['popularity']))
        plt.figure(figsize=GRAPH.FIGURESIZE)
        plt.subplots_adjust(left=0.2, right=0.8)
        plt.barh(data_range, 'popularity', data=self.data,
                 color=[GRAPH.COLOUR_DICT[term] for term in self.data['term']])
        plt.yticks(data_range, self.data['artist_name'])

    def determine_title_suffix(self):
        """Determines the number of terms requested and selects an appropriate string for the title suffix. The
        string is obtained using the DISPLAY_KEY_DICT dictionary, which associates the terms in the 'length_term'
        format with their display-ready format 'Length Term'."""
        list_of_display_ready_terms = [GRAPH.DISPLAY_KEY_DICT[term] for term in self.terms]
        logic_dict = {1: f"{list_of_display_ready_terms[0]}",
                      2: f"{list_of_display_ready_terms[0]} and {list_of_display_ready_terms[-1]}",
                      3: "All Time Ranges"}
        for length in logic_dict:
            if len(list_of_display_ready_terms) == length:
                return logic_dict[length]

    @staticmethod
    def adjust_axes():
        plt.xlim(0, 100)
        plt.xticks(fontsize=GRAPH.TICK['size'], font=GRAPH.TICK['font'], weight=GRAPH.TICK['weight'])
        plt.yticks(fontsize=GRAPH.TICK['size'], font=GRAPH.TICK['font'], weight=GRAPH.TICK['weight'])

    def adjust_labels(self):
        plt.xlabel('Popularity', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'], font=GRAPH.LABEL['font'])
        plt.ylabel('Artist', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'], font=GRAPH.LABEL['font'])
        plt.title(f'Top Artists by Popularity [{self.determine_title_suffix()}]', font=GRAPH.TITLE['font'],
                  size=GRAPH.TITLE['size'], weight=GRAPH.TITLE['weight'])

    def add_elements(self):
        """Adds legend and flavour text elements to the graph."""
        BarElements(*self.terms).return_vertical_lines()
        plt.legend(loc='lower right', handles=BarElements(*self.terms).construct_legend())
        FlavourText(*self.terms).return_flavour_text()

    @staticmethod
    def show_bar():
        plt.show()

    def save_bar(self):
        """Saves the file with a dynamic file name."""
        list_of_suffixes = [term for term in self.terms]
        logic_dict = {1: f"{list_of_suffixes[0]}",
                      2: f"{list_of_suffixes[0]}_and_{list_of_suffixes[-1]}",
                      3: "all_time_ranges"}
        for length in logic_dict:
            if len(list_of_suffixes) == length:
                return plt.savefig(f'spotify_niche_[{logic_dict[length]}].png')
