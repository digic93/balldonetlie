from app.services import PlayerService, TeamService

from flask import  Blueprint, render_template, request, jsonify, url_for, redirect

bp = Blueprint('players', __name__, url_prefix='/jugador')

@bp.route('/', methods=['GET'])
def index():
    return render_template('players/index.html')

@bp.route('/<player_id>', methods=['GET'])
def info(player_id):
    player_service = PlayerService()
    player = player_service.get_by_id(player_id)

    return render_template('players/info.html', player=player)


@bp.route('actualizar/<player_id>', methods=['GET','POST'])
def update(player_id):
    player_service = PlayerService()
    team_service = TeamService()
    
    player = player_service.get_by_id(player_id)
    teams = team_service.get_all_teams()

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        position = request.form.get("position")
        height_feet = float(request.form.get("height_feet"))
        height_inches = float(request.form.get("height_inches"))
        weight_pounds = float(request.form.get("weight_pounds"))
        team_id = int(request.form.get("team"))

        player["first_name"] = first_name
        player["last_name"] = last_name
        player["position"] = position
        player["height_feet"] = height_feet
        player["height_inches"] = height_inches
        player["weight_pounds"] = weight_pounds
        player["team"] = team_service.get_team_by_id(team_id)

        player_service.update(player)

        return redirect(url_for("players.info", player_id=player_id ))



    return render_template('players/update.html', player= player, teams=teams)

@bp.route('/data', methods=['POST'])
def data_table():
    draw = int(request.form.get("draw"))
    start = int(request.form.get("start"))
    length = int(request.form.get("length"))
    search = request.form.get("search[value]")

    player_service = PlayerService()
    players = player_service.get_all_players(length, start, search)

    return jsonify(serialize_data_talbe(players, draw))


def serialize_data_talbe(players, draw):
    data = []
    
    draw = 1 if not draw else draw

    for player in players["data"]:
        show_button = '''
            <a href="''' +  url_for('players.info', player_id= player["id"]) +  '''" class="text-success" >
                Ver <i class="fa fa-eye" aria-hidden="true"></i>
            </a>
        '''
        
        edit_button = '''
            <a href="''' +  url_for('players.update', player_id= player["id"]) +  '''" class="text-primary" >
                <i class="fa fa-pencil" aria-hidden="true"></i> Editar 
            </a>
        '''

        data.append([
                player["first_name"],
                player["last_name"],
                player["position"],
                player["team"]["full_name"],
                player["weight_pounds"],
                show_button,
                edit_button
            ])
    
    return {
            "draw": draw,
            "recordsTotal": players['meta']['total_count'],
            "recordsFiltered": players['meta']['total_count'],
            "data": data
        }
    