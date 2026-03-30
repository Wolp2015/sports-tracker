import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

@patch("app.parse_team")
@patch("app.get_team")
def test_search_team_returns_team_data(mock_get_team, mock_parse_team, client):
    mock_parse_team.return_value = {"name": "Los Angeles Lakers", "league": "NBA"}
    response = client.get("/api/team/Los%20Angeles%20Patriots")
    assert response.status_code == 200
    assert response.get_json() == {"name": "Los Angeles Lakers", "league": "NBA"}

@patch("app.parse_team")
@patch("app.get_team")
def test_search_team_not_found(mock_get_team, mock_parse_team, client):
    mock_parse_team.side_effect = ValueError("Team not found.")
    response = client.get("/api/team/Los%20Angeles%20Patriots")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Team not found."}

@patch("app.parse_player")
@patch("app.get_player")
def test_search_player_returns_player_data(mock_get_player, mock_parse_player, client):
    mock_parse_player.return_value = {"name": "Tom Brady", "league": "NBA"}
    response = client.get("/api/player/Tom%20Brady")
    assert response.status_code == 200
    assert response.get_json() == {"name": "Tom Brady", "league": "NBA"}

@patch("app.parse_player")
@patch("app.get_player")
def test_search_player_not_found(mock_get_player, mock_parse_player, client):
    mock_parse_player.side_effect = ValueError("Player not found.")
    response = client.get("/api/player/Fom Brady")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Player not found."}   