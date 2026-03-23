from database import get_team, save_team, get_player, save_player

fake_team = {
    "name": "Los Angeles Lakers",
    "league": "NBA",
    "stadium": "Crypto.com Arena",
    "location": "Los Angeles, California",
    "formed_year": "1947"
}

fake_player = {
    "id": "12345",
    "player_id": "12345",
    "name": "Tom Brady",
    "team": "Los Angeles Lakers",
    "nationality": "United States",
    "born": "1984-12-30",
    "status": "Active",
    "position": "Small Forward"
}

def test_save_team_returns_an_id(db):
    team_id = save_team(db, fake_team)
    assert isinstance(team_id, int)
    assert team_id > 0

def test_get_team_returns_empty_list(db):
    result = get_team(db)
    assert result == []

def test_save_team_can_be_retrieved(db):
    new_team = save_team(db, fake_team)
    result = get_team(db)
    assert len(result) == 1
    assert result[0]["name"] == "Los Angeles Lakers"

def test_save_player_returns_an_id(db):
    player_id = save_player(db, fake_player)
    assert isinstance(player_id, int)
    assert player_id > 0

def test_get_player_returns_empty_list(db):
    result = get_player(db)
    assert result == []

def test_save_player_can_be_retrieved(db):
    new_player = save_player(db, fake_player)
    result = get_player(db)
    assert len(result) == 1
    assert result[0]["name"] == "Tom Brady"
