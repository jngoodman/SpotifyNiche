from .graph import Bar
from .data_service import DataService


def construct_bar(*args: str, data_service: DataService):
    terms = [*args]
    means = dict(
        (result.term, result.popularity)
        for result in data_service.get_average_popular_artists_by_term()
    )
    data = data_service.get_all_artists_for_terms(terms)

    bar = Bar(terms, means, data)
    bar.construct_bars()
    bar.determine_title_suffix()
    bar.adjust_axes()
    bar.adjust_labels()
    bar.add_elements()
    return bar
