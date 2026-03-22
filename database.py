import sqlite3
def get_connection(db_path=':memory:'):
    return sqlite3.connect(db_path)

def create_table(conn):
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        league TEXT NOT NULL,
        stadium TEXT,
        location TEXT, 
        formed_year TEXT 
        )
        '''
    )

def save_team(conn, team):
    cursor = conn.cursor()
    with conn:
        cursor.execute("INSERT INTO teams (name, league, stadium, location, formed_year) VALUES(?,?,?,?,?)", (team["name"], team["league"], team["stadium"],team["location"],team["formed_year"] ))
    return cursor.lastrowid

def get_teams(conn):
    cursor = conn.cursor()
    select_query = "SELECT id, name, league, stadium, location, formed_year FROM teams"
    cursor.execute(select_query)

    rows = cursor.fetchall()
    teams = []
    for row in rows:
        teams.append({
            "id": row[0],
            "name": row[1],
            "league": row[2],
            "stadium": row[3],
            "location": row[4],
            "formed_year": row[5]
        })
    return teams