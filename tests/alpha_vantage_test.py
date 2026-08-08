import requests

API_KEY = "92HKJHTR2MD6L7MR"

url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "outputsize": "compact",
    "apikey": API_KEY
}

response =  requests.get(url, params=params)

print(response.status_code)
print(response.json())