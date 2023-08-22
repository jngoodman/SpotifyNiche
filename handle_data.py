from statistics import mean
from constants import TERMS


def get_all_terms_subsets(dataframe):
    get_term_subsets = dataframe.groupby(dataframe['ID'])
    return [get_term_subsets.get_group(subset) for subset in TERMS]


def get_means(dataframe, all_terms=False):
    if not all_terms:
        mean_value = round(mean(dataframe['Pops']), 1)
        return mean_value
    else:
        list_of_subsets = get_all_terms_subsets(dataframe)
        mean_values = [round(mean(list_of_subsets[index]['Pops']), 1) for index in range(3)]
        return mean_values
