import psycopg2
import pandas as pd

connection = psycopg2.connect(user="genome",
                              password="genome",
                              host="localhost",
                              port="5432",
                              database="genomes")

table_names = [
    "archaea_ids",
    "bacteria_ids",
    "dsdna_viruses_ids",
    "eukaryota_ids",
    "mito_metazoa_ids",
    "phages_ids",
    "plasmids_ids",
    "samples_ids",
    "viroids_ids",
    "viruses_ids"

]


def get_genomes_ids_csv():
    genomes_id = {}
    for table_name in table_names:
        df = pd.read_sql('SELECT * FROM table_name'.replace('table_name', table_name), connection)
        genomes_id[table_name] = df
    return genomes_id


