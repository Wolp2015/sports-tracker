import pytest
from app import create_app
from database import get_connection, create_table_team, create_table_player

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

@pytest.fixture
def db():
    conn = get_connection()
    create_table_team(conn)
    create_table_player(conn)
    yield conn
    conn.close()