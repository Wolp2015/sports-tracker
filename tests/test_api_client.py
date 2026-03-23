import pytest
from api_client import parse_team, get_team, parse_player, get_player
from unittest.mock import patch

def test_parse_team_returns_correct_fields():
    fake_response = {
        "team": [
            {
            'strTeam': 'Los Angeles Lakers',
            'strLeague': 'NBA',
            'strStadium': 'Crypto.com Arena', 
            'strLocation': 'Los Angeles, California', 
            'intFormedYear': '1947'
            }
        ]
    }

    result = parse_team(fake_response)
    assert result["name"] == "Los Angeles Lakers"
    assert result["league"] == "NBA"
    assert result["stadium"] == "Crypto.com Arena"
    assert result["location"] == "Los Angeles, California"
    assert result["formed_year"] == "1947"

def test_parse_player_returns_correct_fields():
    fake_response = {
        "player": [
            {
            'idPlayer': '34153736', 
            'strPlayer': 'Kobe Bryant', 
            'strTeam': '_Deceased Basketball', 
            'strNationality': 'United States', 
            'dateBorn': '1978-08-23', 
            'strStatus': 'Deceased', 
            'strPosition': 'Shooting Guard'
            }
        ]
    }

    result = parse_player(fake_response)
    assert result["id"] == "34153736"
    assert result["name"] == "Kobe Bryant"
    assert result["team"] == "_Deceased Basketball"
    assert result["nationality"] == "United States"
    assert result["born"] == "1978-08-23"
    assert result["status"] == "Deceased"
    assert result["position"] == "Shooting Guard"

def test_parse_team_raises_error_when_not_found():
    fake_response = {"team": None}
    with pytest.raises(ValueError):
        parse_team(fake_response)

def test_parse_player_raises_error_when_not_found():
    fake_response = {"player": None}
    with pytest.raises(ValueError):
        parse_player(fake_response)

@patch("api_client.requests.get")
def test_get_team_calls_correct_url(mock_get):
    mock_get.return_value.json.return_value = {'team':[0]}
    result = get_team("Los Angeles Lakers")
    mock_get.assert_called_with("https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Los Angeles Lakers")

@patch("api_client.requests.get")
def test_get_player_calls_correct_url(mock_get):
    mock_get.return_value.json.return_value = {'player':[0]}
    result = get_player("Kobe Bryant")
    mock_get.assert_called_with("https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p=Kobe Bryant")