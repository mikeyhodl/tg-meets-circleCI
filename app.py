"""
btc app
"""
import requests

def price():
    """
  btc bot"""
    url = "https://api.coincap.io/v2/rates/bitcoin"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    return response
    