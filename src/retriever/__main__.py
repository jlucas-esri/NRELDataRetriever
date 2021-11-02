import requests
import logging
from retriever.secrets import KEY
import csv

baseUrl = r'https://developer.nrel.gov/api/alt-fuel-stations/v1.csv'


def main():
    payload = {
        'api_key': KEY,
        'limit': 'all'
    }
    response = requests.get(baseUrl, params=payload, verify=False)
    response.raise_for_status()
    csvText = response.content.decode(encoding='cp1252', errors='backslashreplace')
    # print(response.content)
    with open('data.csv', 'w') as f:
        f.write(csvText)
    print('Request successful')

if __name__ == '__main__':
    main()