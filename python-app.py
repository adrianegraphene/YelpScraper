import json
import pandas as pd
import numpy as np
import requests
#from config import api_key1 

#create config.py file with your key, and add a .gitignore file with the name of the credential 
#file (i.e. config.py) so that your key isn't exposed to the world on GitHub if pushing there.
def search_grocers(set_num): 
# This function launches the request for all grocery location endpoints in San Francisco, CA.
    api_key1 = 'Your API Key  here'

    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer {}'.format(api_key1),
    }
    url_params = { #parameters passed to the API
    'term': 'The Best 10 Real Estate Agents',
    "location": "Irvine",
    'sort_by' : "rating",
    'offset': offset_num, # We are going to iterate the offset
     "limit":50 # Maximum return of results per request (ref: API documentation).
     }

    response = requests.get(url, headers=headers, params=url_params)
    return response.json() # Returns a JSON.


if __name__ == "__main__":
    for offset_num in np.arange(50,150,50) : 
# I want up to 550 results, in steps of 50 results per request.
        try:
            output_json = search_grocers(offset_num) # Executing the function defined above.
            print(offset_num) # Making sure each offset iteration is running
         #   print(output_json) # If you wanna check the JSON for each iteration
            if offset_num == 50:
                df_first = pd.DataFrame.from_dict(
                    output_json['businesses']                    
                )
# 'businesses' because that's the primary key of the JSON (i.e. pull all attribute data by calling 
# that one key). This is something you can figure out reading the API documentation or visually
# parsing the JSON. 
            else:
                df2 = pd.DataFrame.from_dict(output_json['businesses'])
                df_first = df_first.append(df2)
# The conditional statement above is so that I can append my results into a single dataframe, to 
# save into a single csv document.
        except AttributeError:
            print("error at ", offset_num) # Helpful for debugging purposes
            
    df_first.to_csv("yelp_data/output_data12.csv", index = False)