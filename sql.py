import os, sqlite3


db_path = 'db.sqlite3'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

search_text = input('Zadej jmeno Pokemona: ')

# "; drop table pokemon_pokemon  --
# select * from pokemon_pokemon where name = ""; drop table pokemon_pokemon  --"
# select * from pokemon_pokemon where name = ""  union select .... --"
# select * from pokemon_pokemon where user_id = 1 or 1 = 1 --"
# !!! zde hrozí SQL Inject
# cursor.execute(f'select * from pokemon_pokemon where name = "{search_text}"')

# zde jsou uživatelské vstupy jako parametry
cursor.execute('select * from pokemon_pokemon where name = ? or name = ?', (search_text, 'další hodnota'))

rows = cursor.fetchall()

for item in rows:
    print(item)


conn.close()
