import requests
import pandas as pd

df_types = pd.read_csv('Data/pokemon_types.csv')

df_damage_type = pd.DataFrame(columns=['type_id','receiver_id','damage_level'])
types = pd.DataFrame(columns=['type_id', 'type_name'])

count = 0

for i in list(df_types.type_id.unique()):
    url = "https://pokeapi.co/api/v2/type/"+str(i)+"/"
    response = requests.get(url).json()
    
    types.loc[len(types)] = [i, response['name']]
    
    for j in range(len(response['damage_relations']['double_damage_to'])):
        df_damage_type.loc[len(df_damage_type)] = [i, 
                                    int(response['damage_relations']['double_damage_to'][j]['url'].split("/")[-2]), 
                                                  2]
        
    for k in range(len(response['damage_relations']['half_damage_to'])):
        df_damage_type.loc[len(df_damage_type)] = [i, 
                                    int(response['damage_relations']['half_damage_to'][k]['url'].split("/")[-2]), 
                                                  0.5]
        
    for l in range(len(response['damage_relations']['no_damage_to'])):
        df_damage_type.loc[len(df_damage_type)] = [i, 
                                    int(response['damage_relations']['no_damage_to'][l]['url'].split("/")[-2]), 
                                                  0]

    count+=1

    if count == 4: 
        df_damage_type.to_csv('Data/damage_type_table.csv', index=False)
        types.to_csv("Data/types.csv", index=False)
        print(i)
        count = 0
    
df_damage_type.to_csv('Data/damage_type_table.csv', index=False)
types.to_csv("Data/types.csv", index=False)