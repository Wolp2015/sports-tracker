from api_client import get_team, parse_team, get_player, parse_player
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

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

    @app.route("/")
    def status():
        return jsonify({"status":"running"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)