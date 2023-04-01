import mysql.connector
import pandas as pd
import numpy as np

def create_db():
    #establishing the connection
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1')
    cursor = conn.cursor()
    
    cursor.execute("DROP database IF EXISTS pokemon") # Dropping database pokemon if already exists.
    
    sql = "CREATE database pokemon"; # Query to create a database
    cursor.execute(sql) # Executing the query

    conn.close() # Closing the connection

def query_pok_table():
    query = '''
        CREATE TABLE pokemon(
        pokemon_id INT NOT NULL,
        pokemon_name CHAR(30),
        height INT,
        weight INT,
        base_experience INT,
        hp INT,
        attack INT,
        defense INT,
        special_attack INT,
        special_defense INT,
        speed INT,
        PRIMARY KEY (pokemon_id)
        )
    '''
    return query 

def query_types():
    query = '''
        CREATE TABLE types(
        type_id INT NOT NULL,
        type_name CHAR(15),
        PRIMARY KEY (type_id)
        )
    '''
    return query  

def query_ability():
    query = '''
        CREATE TABLE ability(
        ability_id INT NOT NULL,
        ability_name CHAR(30),
        PRIMARY KEY (ability_id)
        )
    '''
    return query 

def query_moves():
    query = '''
        CREATE TABLE moves(
        move_id INT NOT NULL,
        move_name CHAR(30),
        accuracy INT,
        pp INT,
        power INT,
        PRIMARY KEY (move_id)
        )
    '''
    return query 

def query_damage_type():
    query = '''
        CREATE TABLE damage_type(
        type_id INT,
        type_reciever_id INT,
        damage_level INT,
        FOREIGN KEY (type_id) REFERENCES types(type_id),
        FOREIGN KEY (type_reciever_id) REFERENCES types(type_id)
        )
    '''
    return query 

def query_evolution():
    query = '''
        CREATE TABLE evolution(
        pokemon_id INT,
        pokemon_evolution_id INT,
        min_level INT,
        evolution_trigger CHAR(20),
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
        FOREIGN KEY (pokemon_evolution_id) REFERENCES pokemon(pokemon_id)
        )
    '''
    return query 

def query_pokemon_ability():
    query = '''
        CREATE TABLE pokemon_ability(
        pokemon_id INT,
        ability_id INT,
        is_hidden BOOL,
        slot INT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
        FOREIGN KEY (ability_id) REFERENCES ability(ability_id)
        )
    '''
    return query 

def query_pokemon_moves():
    query = '''
        CREATE TABLE pokemon_moves(
        pokemon_id INT,
        move_id INT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
        FOREIGN KEY (move_id) REFERENCES moves(move_id)
        )
    '''
    return query 

def query_pokemon_types():
    query = '''
        CREATE TABLE pokemon_types(
        pokemon_id INT,
        type_id INT,
        slot INT,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(pokemon_id),
        FOREIGN KEY (type_id) REFERENCES types(type_id)
        )
    '''
    return query


def create_tables():
    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='pokemon')
    cursor = conn.cursor()

    cursor.execute(query_pok_table())
    cursor.execute(query_ability())
    cursor.execute(query_types())
    cursor.execute(query_moves())
    cursor.execute(query_damage_type())
    cursor.execute(query_evolution())
    cursor.execute(query_pokemon_ability())
    cursor.execute(query_pokemon_moves())
    cursor.execute(query_pokemon_types())
    
    conn.close()

def insert_data():

    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='pokemon')
    cursor = conn.cursor()

    df = pd.read_csv('Data/pokemon_table.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.pokemon VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes
    
    print('Successful')

    df = pd.read_csv('Data/ability.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.ability VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')

    df = pd.read_csv('Data/moves.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.moves VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')

    df = pd.read_csv('Data/types.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.types VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    df = pd.read_csv('Data/evolution_table.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.evolution VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')

    df = pd.read_csv('Data/pokemon_ability.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.pokemon_ability VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')

    df = pd.read_csv('Data/pokemon_moves.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.pokemon_moves VALUES (%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')

    df = pd.read_csv('Data/pokemon_types.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.pokemon_types VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')

    df = pd.read_csv('Data/damage_type_table.csv')
    df1 = df.replace(np.nan, None)
    for i,row in df1.iterrows():
            sql = "INSERT INTO pokemon.damage_type VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            conn.commit()    # the connection is not auto committed by default, so we must commit to save our changes

    print('Successful')
    conn.close()


if __name__ == "__main__":
    create_db()
    create_tables()
    insert_data()


    