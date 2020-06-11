
import json 

from app import path_json_playres

from .abstract_player_resource import AbstractPlayerResource

class PlayerResourceLocal (AbstractPlayerResource):
    
    def get_all(self, per_page: int, page: int) -> dict:  
        return self.__get_json_players()

    def get_by_id(self, id: int) -> dict:
        player = None
        players = self.__get_json_players()
        
        if str(id) in players: 
            player = players[str(id)]

        return player 
    

    def update(self, player: dict) -> dict:
        players = self.__get_json_players()

        players[player["id"]] = player

        self.__set_json_players(players)

        return True
    

    def search(self, search: str, per_page: int, page: int) -> dict:
        result = {}
        players = self.__get_json_players()

        for id_player in players.keys():
            player = players[id_player]

            if search.lower() in  player["first_name"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  player["last_name"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  str(player["height_feet"]):
                result[str(player["id"])] = player

            elif search.lower() in  str(player["height_inches"]):
                result[str(player["id"])] = player

            elif search.lower() in  player["position"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  str(player["weight_pounds"]):
                result[str(player["id"])] = player

            elif search.lower() in  player["team"]["abbreviation"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  player["team"]["city"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  player["team"]["conference"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  player["team"]["division"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  player["team"]["full_name"].lower():
                result[str(player["id"])] = player

            elif search.lower() in  player["team"]["name"].lower():
                result[str(player["id"])] = player                        

        return result


    def __get_json_players(self):
        with open(path_json_playres, 'r') as openfile: 
            json_object = json.load(openfile) 

        return json_object


    def __set_json_players(self, players):
        with open(path_json_playres, "w") as outfile: 
            json.dump(players, outfile) 

        return players
    