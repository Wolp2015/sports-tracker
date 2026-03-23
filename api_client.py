import requests

def get_team(team_name):
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={team_name}")
    return response.json()

def parse_team(response):
    if not response["team"]:
        raise ValueError("Team not found.")
    team = response["team"][0]
    return {
     "name": team["strTeam"],
     "league": team["strLeague"],
     "stadium": team["strStadium"],
     "location": team["strLocation"],
     "formed_year": team["intFormedYear"],
    }

def get_player(p):
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={p}")
    return response.json()
    
def parse_player(response):
    if not response["player"]:
        raise ValueError("Player not found.")
    player = response["player"][0]
    return {
     "id" : player["idPlayer"],
     "name": player["strPlayer"],
     "team": player["strTeam"],
     "nationality": player["strNationality"],
     "born": player["dateBorn"],
     "status": player["strStatus"],
     "position": player["strPosition"]
    }

if __name__ == "__main__":
    while True:
        team_name = input("Enter basketball team name (Example: Los Angeles Lakers): ")
        try:
            team_data = get_team(team_name)
            parsed_team = parse_team(team_data)
            break
        except ValueError as e:
            print(f"Error: {e} Please try again.")

    while True:
        player_name = input("Enter basketball player name: ")
        try:
            player_data = get_player(player_name)
            parsed_player = parse_player(player_data)
            break
        except ValueError as e:
            print(f"Error: {e} Please try again.")
    print(parsed_team)
    print(parsed_player)