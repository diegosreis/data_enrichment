import requests
import logging


class GleifService:
    def __init__(self):
        pass

    @staticmethod
    def call_gleif_api(lei_values, chunk_size):
        lei_string = ','.join(lei_values)
        api_endpoint = f"https://api.gleif.org/api/v1/lei-records?page[size]={chunk_size}&page[number]=1&filter[lei]={lei_string}"
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            return response.json()['data']
        else:
            logging.info(f"Error in API request: {response.status_code}")
            return []
