import requests
import pandas as pd

token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
client_id = '37c8b998-378b-4571-8463-35cee75ab32a_b4e1e58c-5789-43f2-b530-05fbcfb8465d'
client_secret = 'PrqtDYZLv9e9mC14ugsfHh/6IQJCajJ7q2T0twEcOyk='
scope = 'icdapi_access'
grant_type = 'client_credentials'


# get the OAUTH2 token

# set data to post
payload = {'client_id': client_id, 
	   	   'client_secret': client_secret, 
           'scope': scope, 
           'grant_type': grant_type}
           
# make request
r = requests.post(token_endpoint, data=payload, verify=False).json()
token = r['access_token']


# access ICD API
uri = 'https://id.who.int/icd/release/10/2016/D86'

# HTTP header fields to set
headers = {'Authorization':  'Bearer '+token, 
           'Accept': 'application/json', 
           'Accept-Language': 'en',
           'API-Version': 'v2'}

# make request           
r = requests.get(uri, headers=headers, verify=False)

# Check if the request was successful
if r.status_code == 200:
    json_data = r.json()  # Parse the JSON response

    # Convert JSON data to pandas DataFrame
    df = pd.json_normalize(json_data)  # Flatten JSON if it's nested

    # Export DataFrame to Excel
    df.to_excel('icd_diagnosis.xlsx', index=False)
    print("Data exported successfully to 'icd_diagnosis.xlsx'")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {r.status_code}")