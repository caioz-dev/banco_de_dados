import sqlite3

connection = sqlite3.connect('escola.db')
cursor = connection.cursor()

cursor.execute(
    '''
    UPDATE estudantes SET nome = ? WHERE id = ?
    ''',
    ('James', 1)
)

connection.commit()
connection.close()