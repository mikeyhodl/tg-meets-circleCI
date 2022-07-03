import os
import requests
my_secret = os.environ['API_KEY']
my_secret1 = os.environ['CHAT_ID']

api = my_secret
chat_id = my_secret1

def toTg():
	image = "https://images.pexels.com/photos/1580625/pexels-photo-1580625.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

	url = "https://api.telegram.org/bot" + api + "/sendPhoto?chat_id=" + chat_id + "&photo=" + image

	payload={}
	headers = {}
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	
for i in range(1):
	toTg()
