from .team_resource import TeamResource

class TeamService:
    def __init__(self):
        self.team_reasouce = TeamResource()
    

    def get_all_teams(self):
        teams = self.team_reasouce.get_all()
        return teams["data"]

    
    def get_team_by_id(self, team_id):
        return self.team_reasouce.get_by_id(team_id)