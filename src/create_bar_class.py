from matplotlib import pyplot as plt
from .constants import GRAPH
from .flavour_text import FlavourText
from .graph_elements import BarElements


class Bar:

    def __init__(self, dataframe_dict, key):
        self.dataframe = dataframe_dict[key]
        self.key = key

    def construct_bar(self):
        plt.figure(figsize=GRAPH.FIGURESIZE)
        plt.subplots_adjust(left=0.2, right=0.8)
        plt.barh('Names', 'Pops',
                 data=self.dataframe,
                 color=[GRAPH.COLOUR_DICT[i] for i in self.dataframe['ID']])
        plt.xlim(0, 100)
        plt.xticks(fontsize=GRAPH.TICK['size'], font=GRAPH.TICK['font'], weight=GRAPH.TICK['weight'])
        plt.yticks(fontsize=GRAPH.TICK['size'], font=GRAPH.TICK['font'], weight=GRAPH.TICK['weight'])
        plt.xlabel('Popularity', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'], font=GRAPH.LABEL['font'])
        plt.ylabel('Artist', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'], font=GRAPH.LABEL['font'])
        plt.title(f'Top Artists by Popularity [{GRAPH.DISPLAY_KEY_DICT[self.key]}]', font=GRAPH.TITLE['font'],
                  size=GRAPH.TITLE['size'], weight=GRAPH.TITLE['weight'])

    def add_elements(self):
        BarElements(self.dataframe, self.key).return_vertical_lines()
        plt.legend(loc='lower right', handles=BarElements(self.dataframe, self.key).construct_legend())
        FlavourText(self.dataframe, self.key).return_flavour_text()

    @staticmethod
    def show_bar():
        plt.show()
