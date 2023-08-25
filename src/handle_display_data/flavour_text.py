from src.constants.__init__ import GRAPH, TEXT, EXTRACT_VALUES, TERMS
from src.handle_sql_data.__init__ import retrieve_from_db
from matplotlib import pyplot as plt


class FlavourText:
    def __init__(self, *args):
        self.terms = [*args]
        self.means = dict((term, mean) for term, mean in retrieve_from_db(EXTRACT_VALUES.AVG))
        self.most_popular_artists = dict((term, artist) for term, artist, popularity
                                         in retrieve_from_db(EXTRACT_VALUES.MOST))
        self.least_popular_artists = dict((term, artist) for term, artist, popularity
                                          in retrieve_from_db(EXTRACT_VALUES.LEAST))

    def get_direction_of_niche_text(self):
        term_indices = []
        for term in self.terms:
            term_indices.append(TERMS.index(term))
        longest_term = TERMS[max(term_indices)]
        shortest_term = TERMS[min(term_indices)]
        logic_dict = {
            self.means[shortest_term] > self.means[longest_term]:
                f"increased from {round(self.means[longest_term], 1)} to {round(self.means[shortest_term], 1)}",
            self.means[shortest_term] == self.means[longest_term]:
                "stayed the same",
            self.means[shortest_term] < self.means[longest_term]:
                f"decreased from {round(self.means[longest_term], 1)} to {round(self.means[shortest_term], 1)}"
            }
        for expression in logic_dict:
            if expression:
                return logic_dict[expression]

    def _generate_flavour_text(self):
        (subheadings, mean_pop_texts, most_pop_texts, least_pop_texts) = ([], [], [], [])
        for term in self.terms:
            subheadings.append(TEXT.TERM_DICT[term])
            most_pop_texts.append(f'{TEXT.MOST_POPULAR} {self.most_popular_artists[term]}')
            least_pop_texts.append(f'{TEXT.LEAST_POPULAR} {self.least_popular_artists[term]}')
            mean_pop_texts.append(f'{TEXT.POPULARITY} {round(self.means[term], 1)}')
        return {
            "subheadings_list": subheadings,
            "mean_text_list": mean_pop_texts,
            "least_text_list": least_pop_texts,
            "most_text_list": most_pop_texts
        }

    def _get_flavour_text_elements(self):
        flavour_text_dict = self._generate_flavour_text()
        display_text_list = []
        number_of_terms = range(len(flavour_text_dict['subheadings_list']))
        count = 0
        for index in number_of_terms:
            for key in flavour_text_dict:
                if key == 'subheadings_list':
                    weight = GRAPH.TITLE['weight']
                else:
                    weight = GRAPH.TICK['weight']
                display_text_list.append(plt.gcf().text(x=GRAPH.FLAVOUR['x'], y=GRAPH.FLAVOUR['y_list'][count],
                                                        s=flavour_text_dict[key][index], weight=weight,
                                                        font=GRAPH.FLAVOUR['font']))
                count += 1
            count += 2
        if not len(self.terms) == 1:
            direction = self.get_direction_of_niche_text()
            display_text_list.append(plt.gcf().text(x=GRAPH.FLAVOUR['x'], y=GRAPH.FLAVOUR['y_list'][count],
                                                    s=f'{TEXT.DIRECTION_INTRO} {direction}',
                                                    weight=GRAPH.FLAVOUR['weight'],
                                                    font=GRAPH.FLAVOUR['font']))
        return display_text_list

    def return_flavour_text(self):
        self._get_flavour_text_elements()
