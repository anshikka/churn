from utils import auth_utils
import requests

class MasterCardAPI:
    def __init__(self):
        self.oauth = auth_utils.get_oauth()
        self.API = 'https://sandbox.api.mastercard.com'
    
    def build_request_url(self, api_base_url, api_category, api_service, api_endpoint):
        return api_base_url + '/' + api_category + '/' + api_service + '/' + api_endpoint
    
    def get_all_mcc_codes(self):
        API_CATEOGRY = 'location-intelligence'
        API_SERVICE = 'places-locator'
        API_ENDPOINT = 'merchant-category-codes'
        params = {'limit': 10000}
        url = self.build_request_url(self.API, API_CATEOGRY, API_SERVICE, API_ENDPOINT)
        request = requests.get(url, auth=self.oauth, params=params)
        res = request.json()
        data = [[int(item['merchantCategoryCode']), item['merchantCategoryName']] for item in res['items']]
        return data
    
    def get_places(self, radius, long, lat):
        API_CATEGORY = 'location-intelligence'
        API_SERVICE = 'places_locator'
        API_ENDPOINT = 'places/searches'
        params = {'limit': 10000}
        body = {"distance": radius, 
            "place": {
                "latitude": lat,
                "longitude": long
            },
            "radiusSearch": True,
            "unit": "MILE"
        }



class FDICAPI:
    def __init__(self):
        self.API = 'https://banks.data.fdic.gov/api'
    def build_request_url(self, api_base_url, api_endpoint):
        return api_base_url + '/' + api_endpoint
    def get_all_institutions(self):
        API_ENDPOINT = 'institutions'
        params = {'format': 'json', 'limit': 10000, 'fields': ['NAME']}
        url = self.build_request_url(self.API, API_ENDPOINT)
        request = requests.get(url, params=params)
        res = request.json()
        data = [[int(item['data']['ID']), item['data']['NAME']] for item in res['data']]
        return data


        