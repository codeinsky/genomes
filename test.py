insert_row = """
    INSERT INTO %s (id, name, description,sequence ,  %s)
    VALUES ('%s', '%s', '%s', '%s', '%s');
"""


query = (insert_row % ("sausage", "sheep", "id","name", "desc", "seq_test", "column"))
print(query)