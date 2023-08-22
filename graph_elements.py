from handle_data import get_means
from matplotlib import patches, pyplot as plt
from constants import GRAPH, TEXT, ALL_TERMS_FLAG_DICT


class BarElements:
    def __init__(self, dataframe, key):
        self.dataframe = dataframe
        self.key = key
        self.all_terms = ALL_TERMS_FLAG_DICT[key]
        self.means = get_means(self.dataframe, all_terms=self.all_terms)

    def construct_legend(self):
        axes = plt.gca()
        handle_list, labels = axes.get_legend_handles_labels()
        if self.all_terms:
            for key in GRAPH.COLOUR_DICT:
                handle_list.append(patches.Patch(color=GRAPH.COLOUR_DICT[key],
                                                 label=GRAPH.DISPLAY_KEY_DICT[key]))
        return handle_list

    def get_mean_vertical_line(self):
        return [plt.axvline(x=self.means,
                            color='white',
                            linewidth=GRAPH.VLINES['thick']),
                plt.axvline(x=self.means,
                            color=GRAPH.COLOUR_DICT[self.key],
                            linewidth=GRAPH.VLINES['thin'],
                            label='Mean'),
                plt.text(x=self.means + 1, y=0, s=self.means,
                         color=GRAPH.COLOUR_DICT[self.key],
                         weight=GRAPH.VLINES['weight'],
                         size=GRAPH.VLINES['size'],
                         font=GRAPH.VLINES['font']).set_bbox(dict(facecolor=GRAPH.VLINES['bbox'],
                                                                  alpha=.5, edgecolor=GRAPH.VLINES['bbox']))]

    def get_mean_vertical_lines_all_terms(self):
        colour_list = [colour for colour in GRAPH.COLOUR_DICT.values()]
        return [
            [
                plt.axvline(x=self.means[index],
                            color='white',
                            linewidth=GRAPH.VLINES['thick']),
                plt.axvline(x=self.means[index],
                            color=colour_list[index],
                            linewidth=GRAPH.VLINES['thin'],
                            label=f'{TEXT.TERM_LIST[index]} Mean'),
                plt.text(x=self.means[index] + 1, y=0, s=self.means[index],
                         color=colour_list[index],
                         weight=GRAPH.VLINES['weight'],
                         size=GRAPH.VLINES['size'],
                         font=GRAPH.VLINES['font']).set_bbox(dict(facecolor=GRAPH.VLINES['bbox'],
                                                                  alpha=.5, edgecolor=GRAPH.VLINES['bbox']))
            ]
            for index in range(3)
        ]

    def return_vertical_lines(self):
        if self.all_terms:
            self.get_mean_vertical_lines_all_terms()
        else:
            self.get_mean_vertical_line()
