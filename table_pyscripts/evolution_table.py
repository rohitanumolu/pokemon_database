import requests
import pandas as pd

evolution_df = pd.DataFrame(columns=['pokemon_id', 'evolution_pokemon_id', 'min_level','trigger'])
count = 0

for i in range(1,536):
    url = "https://pokeapi.co/api/v2/evolution-chain/"+str(i)+"/"
    response = requests.get(url)
    
    if response.status_code==404:
        print('Not present')
    else: 
        response = response.json()
        r = response['chain']
        
        while(r['evolves_to']):

            id1 = int(r['species']['url'].split("/")[-2])
            
            if r['evolves_to'][0]['evolution_details']:
                min_level = r['evolves_to'][0]['evolution_details'][0]['min_level']
                trigger = r['evolves_to'][0]['evolution_details'][0]['trigger']['name']
            else:
                min_level = None
                trigger = None
                
            id2 = int(r['evolves_to'][0]['species']['url'].split("/")[-2])

            evolution_df.loc[len(evolution_df)] = [id1, id2, min_level, trigger ]
            r = r['evolves_to'][0]

    count += 1 

    if count > 10:
        evolution_df.to_csv("Data/evolution_table.csv", index=False)
        print(i)
        count = 0 
        
evolution_df.to_csv("Data/evolution_table.csv", index=False)