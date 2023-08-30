def read_sql_script(file_path):
    with open(file_path, 'r') as sql_file:
        return sql_file.read()


scripts_dictionary = {
    'create_table': read_sql_script('src/handle_sql_data/sql_commands/create_table.sql'),
    'insert_values': read_sql_script('src/handle_sql_data/sql_commands/insert_values.sql'),
    'get_averages': read_sql_script('src/handle_sql_data/sql_commands/get_averages.sql'),
    'get_least': read_sql_script('src/handle_sql_data/sql_commands/get_least_popular.sql'),
    'get_most': read_sql_script('src/handle_sql_data/sql_commands/get_most_popular.sql'),
}

