from create_bar_class import Bar
from store_artist_data import get_dataframes


def main():
    bar = Bar(dataframe_dict=get_dataframes(), key='medium_term')
    bar.construct_bar()
    bar.add_elements()
    bar.show_bar()


if __name__ == "__main__":
    main()
