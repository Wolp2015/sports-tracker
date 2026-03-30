import sqlite3
def get_connection(db_path=':memory:'):
    return sqlite3.connect(db_path)

def create_table_team(conn):
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        league TEXT NOT NULL,
        stadium TEXT,
        location TEXT, 
        formed_year TEXT 
        )
        '''
    )

def create_table_player(conn):
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id TEXT,
        name TEXT NOT NULL,
        team TEXT,
        nationality TEXT,
        born TEXT,
        status TEXT, 
        position TEXT 
        )
        '''
    )
def save_team(conn, team):
    cursor = conn.cursor()
    with conn:
        cursor.execute("INSERT INTO team (name, league, stadium, location, formed_year) VALUES(?,?,?,?,?)", (team["name"], team["league"], team["stadium"],team["location"],team["formed_year"] ))
    return cursor.lastrowid

def save_player(conn, player):
    cursor = conn.cursor()
    with conn:
        cursor.execute("INSERT INTO player (player_id, name, team, nationality, born, status, position) VALUES(?,?,?,?,?,?,?)", (player["player_id"], player["name"],player["team"],player["nationality"], player["born"], player["status"], player["position"] ))
    return cursor.lastrowid

def get_saved_team(conn):
    cursor = conn.cursor()
    select_query = "SELECT id, name, league, stadium, location, formed_year FROM team"
    cursor.execute(select_query)

    rows = cursor.fetchall()
    team = []
    for row in rows:
        team.append({
            "id": row[0],
            "name": row[1],
            "league": row[2],
            "stadium": row[3],
            "location": row[4],
            "formed_year": row[5]
        })
    return team

def get_saved_player(conn):
    cursor = conn.cursor()
    select_query = "SELECT player_id, name, team, nationality, born, status, position FROM player"
    cursor.execute(select_query)

    rows = cursor.fetchall()
    player = []
    for row in rows:
        player.append({
            "player_id": row[0],
            "name": row[1],
            "team": row[2],
            "nationality": row[3],
            "born": row[4],
            "status": row[5],
            "position": row[6]
        })
    return player