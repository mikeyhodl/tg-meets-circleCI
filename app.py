import requests

def Price():
  url = "https://api.coincap.io/v2/rates/bitcoin"
  payload={}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)

  return response
  
  print(response.text)

# import requests

# url = "https://api.coincap.io/v2/assets/bitcoin"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)