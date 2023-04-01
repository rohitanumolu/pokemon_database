import requests
import pandas as pd

df_ability= pd.read_csv('Data/pokemon_ability.csv')

ability = pd.DataFrame(columns=['ability_id', 'ability_name'])

count = 0

for i in list(df_ability.ability_id.unique()):
    url = "https://pokeapi.co/api/v2/ability/"+str(i)+"/"
    response = requests.get(url).json()
    
    ability.loc[len(ability)] = [i, response['name']]

    count+=1

    if count == 10: 
        ability.to_csv('Data/ability.csv', index=False)
        print(i)
        count = 0

ability.to_csv('Data/ability.csv', index=False)