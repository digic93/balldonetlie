
class AbstractPlayerResource:
    def get_all(self, per_page: int, page: int) -> dict:
        pass
    
    def get_by_id(self, id: int) -> dict:
        pass
    
    def update(self, player: dict) -> dict:
        pass
    
    def search(self, search: str, per_page: int, page: int) -> dict:
        pass
    