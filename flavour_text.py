from constants import GRAPH, TEXT, ALL_TERMS_FLAG_DICT
from handle_data import get_means, get_all_terms_subsets
from matplotlib import pyplot as plt


class MeanCompare:
    short_term_mean: int
    long_term_mean: int

    def __init__(self, short_term_mean, long_term_mean):
        self.short_term_mean = short_term_mean
        self.long_term_mean = long_term_mean

    def get_statement(self):
        logic_dict = {
            self.short_term_mean > self.long_term_mean: f'increased from {self.long_term_mean} to {self.short_term_mean}',
            self.short_term_mean == self.long_term_mean: 'stayed the same',
            self.short_term_mean < self.long_term_mean: f'decreased from {self.long_term_mean} to {self.short_term_mean}'
        }
        for expression in logic_dict:
            if expression:
                return logic_dict[expression]


class FlavourText:
    def __init__(self, dataframe, key):
        self.dataframe = dataframe
        self.key = key
        self.all_terms = ALL_TERMS_FLAG_DICT[key]
        self.means = get_means(self.dataframe, all_terms=self.all_terms)

    def _generate_flavour_text(self):
        if not self.all_terms:
            mean_pop_text = f"{TEXT.POPULARITY} {self.means}"
            [most_pop_artist, least_pop_artist] = [self.dataframe.loc[self.dataframe['Pops'].idxmax(), 'Names'],
                                                   self.dataframe.loc[self.dataframe['Pops'].idxmin(), 'Names']]
            most_pop_text = f'{TEXT.MOST_POPULAR} {most_pop_artist}'
            least_pop_text = f'{TEXT.LEAST_POPULAR} {least_pop_artist}'
            return {
                "mean_text": mean_pop_text,
                "least_text": least_pop_text,
                "most_text": most_pop_text
            }

    def _generate_flavour_text_all_terms(self):
        list_of_subsets = get_all_terms_subsets(self.dataframe)
        (subheadings, mean_pop_texts, most_pop_texts, least_pop_texts) = ([], [], [], [])
        for index in range(3):
            subheadings.append(TEXT.TERM_LIST_EXT[index])
            [most_pop_artist, least_pop_artist] = [
                list_of_subsets[index].loc[list_of_subsets[index]['Pops'].idxmax(), 'Names'],
                list_of_subsets[index].loc[list_of_subsets[index]['Pops'].idxmin(), 'Names']
            ]
            most_pop_texts.append(f'{TEXT.MOST_POPULAR} {most_pop_artist}')
            least_pop_texts.append(f'{TEXT.LEAST_POPULAR} {least_pop_artist}')
            mean_pop_texts.append(f'{TEXT.POPULARITY} {self.means[index]}')
        return {
            "subheadings_list": subheadings,
            "mean_text_list": mean_pop_texts,
            "least_text_list": least_pop_texts,
            "most_text_list": most_pop_texts
        }

    def _get_flavour_text_elements(self):
        flavour_text_dict = self._generate_flavour_text()
        if not self.all_terms:
            return [plt.gcf().text(x=GRAPH.FLAVOUR['x'], y=GRAPH.FLAVOUR['y_list'][0], s=flavour_text_dict['most_text'],
                                   font=GRAPH.VLINES['font']),
                    plt.gcf().text(x=GRAPH.FLAVOUR['x'], y=GRAPH.FLAVOUR['y_list'][1],
                                   s=flavour_text_dict['least_text'],
                                   font=GRAPH.VLINES['font']),
                    plt.gcf().text(x=GRAPH.FLAVOUR['x'], y=GRAPH.FLAVOUR['y_list'][2], s=flavour_text_dict['mean_text'],
                                   font=GRAPH.VLINES['font'])]

    def _get_flavour_text_elements_all_terms(self):
        flavour_text_dict = self._generate_flavour_text_all_terms()
        display_text_list = []
        count = 0
        for index in range(3):
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
        direction = MeanCompare(self.means[0], self.means[2]).get_statement()
        display_text_list.append(plt.gcf().text(x=GRAPH.FLAVOUR['x'], y=GRAPH.FLAVOUR['y_list'][count],
                                                s=f'{TEXT.DIRECTION_INTRO} {direction}',
                                                weight=GRAPH.FLAVOUR['weight'],
                                                font=GRAPH.FLAVOUR['font']))
        return display_text_list

    def return_flavour_text(self):
        if self.all_terms:
            self._get_flavour_text_elements_all_terms()
        else:
            self._get_flavour_text_elements()
