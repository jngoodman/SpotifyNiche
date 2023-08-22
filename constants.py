from numpy import arange

TERMS = ['short_term', 'medium_term', 'long_term']


class GRAPH:
    TITLE = {
        'size': 24,
        'weight': 'bold',
        'font': 'Arial'
    }
    LABEL = {
        'size': 16,
        'weight': 'bold',
        'font': 'Arial'
    }
    TICK = {
        'size': 10,
        'font': 'Arial',
        'weight': 'normal'
    }
    FIGURESIZE = (18, 8)
    COLOUR_DICT = {
        'short_term': 'red',
        'medium_term': 'blue',
        'long_term': 'green'
    }
    DISPLAY_KEY_DICT = {
        'short_term': 'Short Term',
        'medium_term': 'Medium Term',
        'long_term': 'Long Term',
        'all_terms': 'All Time Ranges'
    }
    VLINES = {
        'thin': 3,
        'thick': 6,
        'weight': 'bold',
        'size': 12,
        'font': 'Arial',
        'bbox': 'white'
    }
    FLAVOUR = {
        'x': 0.81,
        'y_list': arange(0.81, 0, -.03),
        'font': 'Arial',
        'weight': 'normal'
    }


class TEXT:
    TERM_LIST = ['Short Term', 'Medium Term', 'Long Term']
    TERM_LIST_EXT = ['Short Term (~4 weeks)', 'Medium Term (~6 months)', 'Long Term (>1 year)']
    MOST_POPULAR = "Most popular top artist:"
    LEAST_POPULAR = "Least popular top artist:"
    POPULARITY = "Average popularity:"
    DIRECTION_INTRO = "The average popularity of your top artists " \
                      "\nhas"


ALL_TERMS_FLAG_DICT = {
    'all_terms': True,
    'short_term': False,
    'long_term': False,
    'medium_term': False
}

