from matplotlib import patches, pyplot as plt
from constants import GRAPH, EXTRACT_VALUES
from handle_sql_data import retrieve_from_db


class BarElements:
    def __init__(self, *args: str):
        self.terms: list = [*args]
        self.means: dict = dict(
            (term, mean) for term, mean in retrieve_from_db(EXTRACT_VALUES.AVG)
        )

    def construct_legend(self):
        """Composes a legend from automatically-generated legends (vertical lines) and a manually generated legend
        for the bars. Manual generation is to prevent individual legend entries for each bar, since bars are coloured
        entry-by-entry."""
        axes = plt.gca()
        handle_list, labels = axes.get_legend_handles_labels()
        for term in self.terms:
            handle_list.append(
                patches.Patch(
                    color=GRAPH.COLOUR_DICT[term], label=GRAPH.DISPLAY_KEY_DICT[term]
                )
            )
        return handle_list

    def _get_mean_vertical_lines(self):
        """Gets vertical lines representing means for each term in self.terms."""
        vertical_lines_list = []
        for term in self.terms:
            vertical_lines_list.append(
                plt.axvline(
                    x=self.means[term], color="white", linewidth=GRAPH.VLINES["thick"]
                )
            )
            vertical_lines_list.append(
                plt.axvline(
                    x=self.means[term],
                    color=GRAPH.COLOUR_DICT[term],
                    linewidth=GRAPH.VLINES["thin"],
                    label=f"{GRAPH.DISPLAY_KEY_DICT[term]} Mean",
                )
            )
            vertical_lines_list.append(
                plt.text(
                    x=self.means[term] + 1,
                    y=0,
                    s=round(self.means[term], 1),
                    color=GRAPH.COLOUR_DICT[term],
                    weight=GRAPH.VLINES["weight"],
                    size=GRAPH.VLINES["size"],
                    font=GRAPH.VLINES["font"],
                ).set_bbox(
                    dict(
                        facecolor=GRAPH.VLINES["bbox"],
                        alpha=0.5,
                        edgecolor=GRAPH.VLINES["bbox"],
                    )
                )
            )
        return vertical_lines_list

    def return_vertical_lines(self):
        self._get_mean_vertical_lines()
