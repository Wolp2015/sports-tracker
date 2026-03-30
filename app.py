from flask_cors import CORS
from api_client import get_team, parse_team, get_player, parse_player
from flask import Flask, jsonify
from database import get_connection, create_table_team, create_table_player, save_team, save_player, get_saved_team, get_saved_player

def create_app():
    app = Flask(__name__)
    CORS(app)
    conn = get_connection("sports_tracker.db")
    create_table_team(conn)
    create_table_player(conn)
    app.db = conn
        
    @app.route("/api/team/<path:team_name>")
    def search_team(team_name):
        try:
            team_data = get_team(team_name)
            parsed_team = parse_team(team_data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        return jsonify(parsed_team)

    @app.route("/api/player/<path:player>")
    def search_player(player):
        try:
            player_data = get_player(player)
            parsed_player = parse_player(player_data)
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        return jsonify(parsed_player)

    @app.route("/api/team/save/<path:team_name>", methods=["POST"])
    def save_team_route(team_name):
        try:
            team_data = get_team(team_name)
            parsed_team = parse_team(team_data)
            team_id = save_team(app.db, parsed_team)    
            parsed_team["id"] = team_id   
            return jsonify(parsed_team)
        
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        
    @app.route("/api/player/save/<path:player_name>", methods=["POST"])
    def save_player_route(player_name):
        try:
            player_data = get_player(player_name)
            parsed_player = parse_player(player_data)
            player_id = save_player(app.db, parsed_player)    
            parsed_player["id"] = player_id   
            return jsonify(parsed_player)
        
        except ValueError as e:
            return jsonify({"error": str(e)}), 404    
    
    @app.route("/api/teams")
    def list_teams():
        result = get_saved_team(app.db)
        return jsonify(result)

    @app.route("/api/players")
    def list_players():
        result = get_saved_player(app.db)
        return jsonify(result)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)