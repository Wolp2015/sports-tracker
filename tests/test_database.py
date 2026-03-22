import pytest
from database import get_teams, save_team, get_connection, create_table


fake_team = {
    "name": "Los Angeles Lakers",
    "league": "NBA",
    "stadium": "Crypto.com Arena",
    "location": "Los Angeles, California",
    "formed_year": "1947"
}

@pytest.fixture
def db():
    conn = get_connection()
    create_table(conn)
    yield conn
    conn.close()

def test_save_team_returns_an_id(db):
    team_id = save_team(db, fake_team)
    assert isinstance(team_id, int)
    assert team_id > 0

def test_get_teams_returns_empty_list(db):
    result = get_teams(db)
    assert result == []

def test_save_team_can_be_retrieved(db):
    new_team = save_team(db, fake_team)
    result = get_teams(db)
    assert len(result) == 1
    assert result[0]["name"] == "Los Angeles Lakers"
