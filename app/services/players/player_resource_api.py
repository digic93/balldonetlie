import requests


from .abstract_player_resource import AbstractPlayerResource

class PlayerResourceApi(AbstractPlayerResource):
    def __init__(self):
        super(PlayerResourceApi,self).__init__()
        self.__base_curl =  "https://www.balldontlie.io/api/v1/players"

    def get_all(self, per_page, page) -> dict:
        result = None
        params = {
            "page": page,
            "per_page": per_page,
        }
        response = requests.get(self.__base_curl, params=params)
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


    def update(self, player: dict) -> dict:
        pass


    def search(self, search: str, per_page: int, page: int) -> dict:
        params = {
            "page": page,
            "per_page": per_page,
            "search": search
        }

        response = requests.get(self.__base_curl, params=params).json()
        
        return response


    