from .player_resource_api import PlayerResourceApi
from .player_resource_local import PlayerResourceLocal
from .abstract_player_resource import AbstractPlayerResource

class PlayerFactory:

    def get_players_api(self) -> AbstractPlayerResource:
        return PlayerResourceApi()

    def get_players_local(self) -> AbstractPlayerResource:
        return PlayerResourceLocal()