import psycopg2
import queries

connection = psycopg2.connect(user="genome",
                              password="genome",
                              host="localhost",
                              port="5432",
                              database="genomes")


def create_mapping_table(table_name):
    print('Creating table:', table_name )
    if '/' in table_name:
        table_details_list = table_name.split('/')
        table_name = table_details_list[-1]
    if '.' in table_name:
        table_name = table_name.replace('.', '_')
    else:
        table_name = table_name
    cursor = connection.cursor()
    query = (queries.create_table_mapping % table_name)
    cursor.execute(query)
    connection.commit()
    # print("Table created:", table_name)


def create_column_mapping(table_name, column_name):
    if '/' in table_name:
        table_details_list = table_name.split('/')
        table_name = table_details_list[-1]
    if '.' in table_name:
        table_name = table_name.replace('.', '_')
    else:
        table_name = table_name
    column_name = column_name.replace('.', '_').replace('-','_')
    query = (queries.add_column % (table_name, column_name))
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except (Exception, psycopg2.Error) as error:
        print("This column already exists", error)
    # print("Column added:", column_name)
    connection.commit()


def add_record_to_mapping(table_name, id, name, description, seq, column_name, column_value):
    if '/' in table_name:
        table_details_list = table_name.split('/')
        table_name = table_details_list[-1]
    if '.' in table_name:
        table_name = table_name.replace('.', '_')
    else:
        table_name = table_name
    query = (queries.insert_row_mapping % (table_name, id.replace('.', '_').replace('-','_'), name, description, seq, column_name, column_value))
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Table name add:", table_name)
        print("ID:", id)
        print("Column value" , column_value)
    except (Exception, psycopg2.Error) as error:
        print("Failed add record to mapping", error)
    connection.commit()


def add_existing_row_record_to_mapping(table_name, id, name, description, seq, column_name, column_value):
    if '/' in table_name:
        table_details_list = table_name.split('/')
        table_name = table_details_list[2] + '__probe_mapping'
    else:
        table_name = table_name
    query = queries.add_value_where_condition % (table_name, id, column_value, 'id', name)
    print(query)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Added data to existed row")
    except (Exception, psycopg2.Error) as error:
        print("Failed add record to mapping", error)
    connection.commit()

# UPDATE %s
# SET %s = %s
# WHERE %s = %s;


