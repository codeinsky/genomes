create_table_mapping = """
CREATE TABLE IF NOT EXISTS %s (
            id VARCHAR(255),
            name VARCHAR(255),
            description VARCHAR(255), 
            sequence VARCHAR(255)
        )
"""

create_table_results = """
CREATE TABLE IF NOT EXISTS %s (
            probe_id VARCHAR(255)
        )
"""



add_column = """
    ALTER TABLE %s
    ADD COLUMN %s VARCHAR(255);
"""

insert_row_mapping = """
    INSERT INTO %s (id, name, description,sequence ,  %s)
    VALUES ('%s', '%s', '%s', '%s', '%s');
"""

insert_row_result = """
    INSERT INTO %s (probe_id, %s)
    VALUES ('%s', '%s');
"""

add_value_where_condition = """
UPDATE %s
SET %s = '%s'
WHERE %s = '%s';
"""