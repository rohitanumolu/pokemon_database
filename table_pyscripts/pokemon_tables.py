import requests
import pandas as pd

## Base pokemon table
df_base = pd.DataFrame(columns= ['pokemon_id', 'pokemon_name', 'height', 'weight','base_experience','hp','attack','defense','special-attack',
                  'special-defense', 'speed' ])

## Abilities table
df_ability = pd.DataFrame(columns=['pokemon_id', 'ability_id', 'is_hidden', 'slot'])

## Pokemon types table
df_types = pd.DataFrame(columns=['pokemon_id', 'type_id', 'slot'])

## Moves table
df_moves = pd.DataFrame(columns=['pokemon_id', 'move_id'])

count = 0

for j in range(1,1008):
    url = "https://pokeapi.co/api/v2/pokemon/"+str(j)+"/"
    response = requests.get(url).json()

    df_base.loc[len(df_base)] = [
                response['id'], response['name'], response['height'], response['weight'], response['base_experience'], 
                response['stats'][0]['base_stat'], response['stats'][1]['base_stat'], response['stats'][2]['base_stat'],
                response['stats'][3]['base_stat'], response['stats'][4]['base_stat'], response['stats'][5]['base_stat']
               ]
    
    
    for i in range(len(response['abilities'])):
        df_ability.loc[len(df_ability)] = [
                                    response['id'], int(response['abilities'][i]['ability']['url'].split("/")[-2]),
                                    response['abilities'][i]['is_hidden'], 
                                    response['abilities'][i]['slot']  ]
        
    
    for i in range(len(response['types'])):
        df_types.loc[len(df_types)] = [
                                    response['id'], int(response['types'][i]['type']['url'].split("/")[-2]), response['types'][i]['slot'] ]
                
        
    for i in range(len(response['moves'])):
        df_moves.loc[len(df_moves)] = [
                                    response['id'], int(response['moves'][i]['move']['url'].split("/")[-2])]

    count += 1 

    if count == 50:
        df_base.to_csv('Data/pokemon_table.csv', index=False)
        df_ability.to_csv('Data/pokemon_ability.csv', index=False)
        df_types.to_csv('Data/pokemon_types.csv', index=False)
        df_moves.to_csv('Data/pokemon_moves.csv', index=False)
        
        print(j)
        count = 0 
        #time.sleep(30)

df_base.to_csv('Data/pokemon_table.csv', index=False)
df_ability.to_csv('Data/pokemon_ability.csv', index=False)
df_types.to_csv('Data/pokemon_types.csv', index=False)
df_moves.to_csv('Data/pokemon_moves.csv', index=False)
