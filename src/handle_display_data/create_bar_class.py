from matplotlib import pyplot as plt
from src.constants.__init__ import GRAPH, EXTRACT_VALUES
from src.handle_sql_data.__init__ import retrieve_from_db
from src.handle_display_data.flavour_text import FlavourText
from src.handle_display_data.graph_elements import BarElements


class Bar:

    def __init__(self, *args):
        self.terms = [*args]
        self.data = None

    def extract_data(self):
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
        """Note normally you would plt.barh(x, y) but with duplicate artist_names it is necessary to plot popularity on
        its range instead, which prevents pyplot's default deletion of duplicate artist_names. You can then just rename
        the yticks to the entries in artist_name afterwards."""
        data_range = range(len(self.data['popularity']))
        plt.figure(figsize=GRAPH.FIGURESIZE)
        plt.subplots_adjust(left=0.2, right=0.8)
        plt.barh(data_range, 'popularity', data=self.data,
                 color=[GRAPH.COLOUR_DICT[term] for term in self.data['term']])
        plt.yticks(data_range, self.data['artist_name'])

    def determine_display_key(self):
        display_key_list = [GRAPH.DISPLAY_KEY_DICT[term] for term in self.terms]
        logic_dict = {1: f"{display_key_list[0]}",
                      2: f"{display_key_list[0]} and {display_key_list[-1]}",
                      3: "All Time Ranges"}
        for length in logic_dict:
            if len(display_key_list) == length:
                return logic_dict[length]

    @staticmethod
    def adjust_axes():
        plt.xlim(0, 100)
        plt.xticks(fontsize=GRAPH.TICK['size'], font=GRAPH.TICK['font'], weight=GRAPH.TICK['weight'])
        plt.yticks(fontsize=GRAPH.TICK['size'], font=GRAPH.TICK['font'], weight=GRAPH.TICK['weight'])

    def adjust_labels(self):
        plt.xlabel('Popularity', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'], font=GRAPH.LABEL['font'])
        plt.ylabel('Artist', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'], font=GRAPH.LABEL['font'])
        plt.title(f'Top Artists by Popularity [{self.determine_display_key()}]', font=GRAPH.TITLE['font'],
                  size=GRAPH.TITLE['size'], weight=GRAPH.TITLE['weight'])

    def add_elements(self):
        BarElements(*self.terms).return_vertical_lines()
        plt.legend(loc='lower right', handles=BarElements(*self.terms).construct_legend())
        FlavourText(*self.terms).return_flavour_text()

    @staticmethod
    def show_bar():
        plt.show()
