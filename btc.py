import os
import requests
import json
from dotenv.main import load_dotenv
from app import Price
response = Price()
load_dotenv()

mykey = os.environ['API_KEY']
myid = os.environ['CHAT_ID']

loaded_r = json.loads(response.text)
data = loaded_r["data"]["rateUsd"]
id = loaded_r["data"]["id"]
symbol = loaded_r["data"]["symbol"]
currencySymbol = loaded_r["data"]["currencySymbol"]

final = (data)
print(final)
print(response.text)

def Totg():
  url = 'https://api.telegram.org/bot' + mykey + '/sendMessage?chat_id=' + myid + '&text=' + 'The price of '+ currencySymbol + ' is' + ' :' + ' ' + str(final)
  myobj = {'somekey': 'somevalue'}
  
  x = requests.post(url, json = myobj)
  
  print(x.status_code)
