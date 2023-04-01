import requests
import pandas as pd

df_moves = pd.read_csv('Data/pokemon_moves.csv')

moves = pd.DataFrame(columns=['move_id', 'move_name', 'accuracy', 'pp', 'power'])

count = 0

for i in list(df_moves.move_id.unique()):
    url = "https://pokeapi.co/api/v2/move/"+str(i)+"/"
    response = requests.get(url).json()
    
    moves.loc[len(moves)] = [i, response['name'], response['accuracy'], response['pp'], response['power']]

    count+=1

    if count == 10: 
        moves.to_csv('Data/moves.csv', index=False)
        print(i)
        count = 0
        
moves.to_csv('Data/moves.csv', index=False)