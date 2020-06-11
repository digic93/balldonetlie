import requests

class TeamResource:
    def __init__(self):
        super(TeamResource,self).__init__()
        self.__base_curl =  "https://balldontlie.io/api/v1/teams"

    def get_all(self) -> dict:
        result = None
        
        response = requests.get(self.__base_curl)
        if response.status_code == 200:
            result = response.json()
        elif response.status_code == 404:
            result = None
        
        return result
   

    def get_by_id(self, id: int) -> dict:            
        result = None
        url = self.__base_curl + "/" + str(id)
        
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
        elif response.status_code == 404:
            result = None

        return result