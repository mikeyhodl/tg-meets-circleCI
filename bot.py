import requests

api = "APIHERE"

def toTg():
	image = "https://images.pexels.com/photos/1580625/pexels-photo-1580625.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

	url = "https://api.telegram.org/bot" + api + "/sendPhoto?chat_id=IDHERE&photo=" + image
	payload={}
	headers = {}
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	dataa = response.text
	
for i in range(1):
	toTg()

