from get_artist_data import GetArtistData
from pandas import DataFrame, concat


def get_pops(term):
    return [pop for pop in GetArtistData().get_pops_by_term(term)]


def get_names(term):
    name_prefix = {
        'short_term': '',
        'medium_term': ' ',
        'long_term': '  '
    }
    return [name_prefix[term] + name for name in GetArtistData().get_names_by_term(term)]


def get_len(term):
    return len([name for name in GetArtistData().get_names_by_term(term)])


def get_dataframes():
    short_term = DataFrame({'Names': get_names('short_term'),
                            'Pops': get_pops('short_term'),
                            'ID': ['short_term'] * get_len('short_term')}).sort_values('Pops')
    medium_term = DataFrame({'Names': get_names('medium_term'),
                             'Pops': get_pops('medium_term'),
                             'ID': ['medium_term'] * get_len('medium_term')}).sort_values('Pops')
    long_term = DataFrame({'Names': get_names('long_term'),
                           'Pops': get_pops('long_term'),
                           'ID': ['long_term'] * get_len('long_term')}).sort_values('Pops')
    return {
        'short_term': short_term,
        'medium_term': medium_term,
        'long_term': long_term,
        'all_terms': concat([short_term, medium_term, long_term]).sort_values('Pops')
    }
