from .player_factory import PlayerFactory

class PlayerService:
    def __init__(self):
        player_factory = PlayerFactory()
        self.__player_resource_api = player_factory.get_players_api()
        self.__player_resource_local = player_factory.get_players_local()

    
    def get_all_players(self, per_page, start, search):
        if start < per_page:
            page = 1  
        elif start == per_page:
            page = 2  
        else:
            page = int(start / per_page)  
        

        if search:
            players_api = self.__player_resource_api.search(search, per_page, page)
            players_local = self.__player_resource_local.search(search, per_page, page)
        else:
            players_api = self.__player_resource_api.get_all(per_page, page)
            players_local = self.__player_resource_local.get_all(per_page, page)
           

        return self.__get_final_playesr(players_api, players_local)

    def get_by_id(self, player_id):
        local_player = self.__player_resource_local.get_by_id(player_id)
        
        return local_player if local_player else self.__player_resource_api.get_by_id(player_id)


    def update(self, player):
        self.__player_resource_local.update(player)


    def __get_final_playesr(self, players_api, players_local):
        players = []
        aux_id_local_players = [] 
        final_players = {
                "meta": players_api["meta"]
            }

        for player_api in players_api["data"]:
            if str(player_api["id"]) in list(players_local.keys()):
                players.append(players_local[str(player_api["id"])])
                aux_id_local_players.append(str(player_api["id"]))
            else:
                players.append(player_api)

        local_players_out = set (list(players_local.keys())) - set(aux_id_local_players)
        for id_player in local_players_out:
            players.append(players_local[id_player])
        
        final_players["data"] = players
    
        return final_players
                
        