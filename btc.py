"""
btc bot
"""
import os
import json
import requests
from dotenv.main import load_dotenv
from app import price
response = price()
load_dotenv()

mykey = os.environ['API_KEY']
myid = os.environ['CHAT_ID']

loaded_r = json.loads(response.text)
btcdata = loaded_r["data"]["rateUsd"]
btcid = loaded_r["data"]["id"]
symbol = loaded_r["data"]["symbol"]
currencySymbol = loaded_r["data"]["currencySymbol"]

final = (btcdata)

def to_tg():
    """
  Send message to Telegram"""
    url = 'https://api.telegram.org/bot' + mykey + '/sendMessage?chat_id=' \
    + myid + '&text=' + 'The price of '+ currencySymbol + ' is' + ' :' + ' ' + str(final)
    myobj = {'somekey': 'somevalue'}
    result = requests.post(url, json = myobj)
    print(result.status_code)

    return " "
