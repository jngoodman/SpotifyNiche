from dataclasses import dataclass

TERMS = ['short_term', 'medium_term', 'long_term']


@dataclass
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
        'font': 'Arial'
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
            'long_term': 'Long Term'
    }
