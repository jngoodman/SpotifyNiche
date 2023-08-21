from statistics import mean
from matplotlib import pyplot as plt, patches
from store_artist_data import get_dataframes, get_pops, get_names
from constants import GRAPH


class Bar:

    def __init__(self, data):
        self.dataframe_dictionary: dict = data

    @staticmethod
    def construct_legend(key, all_terms=False):
        legend_list = []
        if all_terms:
            for key in GRAPH.DISPLAY_KEY_DICT:
                legend_list.append(patches.Patch(color=GRAPH.COLOUR_DICT[key],
                                                 label=GRAPH.DISPLAY_KEY_DICT[key]))
        else:
            legend_list.append(patches.Patch(color=GRAPH.COLOUR_DICT[key],
                                             label=GRAPH.DISPLAY_KEY_DICT[key]))

    def construct_bar(self, key):
        plt.figure(figsize=GRAPH.FIGURESIZE)
        plt.barh('Names', 'Pops',
                 data=self.dataframe_dictionary[key],
                 color=[GRAPH.COLOUR_DICT[i] for i in self.dataframe_dictionary[key]['ID']])
        plt.xlabel('Popularity', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'])
        plt.ylabel('Artist', size=GRAPH.LABEL['size'], weight=GRAPH.LABEL['weight'])
        plt.title('Top Artists by Popularity', size=GRAPH.TITLE['size'], weight=GRAPH.TITLE['weight'])
        if key == 'all_terms':
            plt.legend(loc='lower right', handles=self.construct_legend(key, all_terms=True))
        plt.show()


Bar(data=get_dataframes()).construct_bar(key='short_term')
