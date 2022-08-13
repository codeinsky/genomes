import pandas as pd
import psycopg2
import glob
import loadGenomesIdsToCSV
from sqlalchemy import create_engine

loadGenomesIdsToCSV.textDataSheetToCSV()


def store_sql():
    engine = create_engine('postgresql://genome:genome@localhost:5432/genomes')
    genome_csv_files = glob.glob("./genomeIdCsv/*")
    for csv_file in genome_csv_files:
        table_name = (csv_file.split('/')[2].split('.')[0] + '_ids').lower()
        data_frame = pd.read_csv(csv_file)
        data_frame.to_sql(table_name, engine, index=False)


store_sql()
