from typing import List, Any
import string
alphabet = string.ascii_letters + string.digits

# Temporary until records database completely set.
# Master database

"""
Game ID |    UID    |  F_name |  L_name |
--------|-----------|---------|---------|
"""

# per game database
"""
|    UID    |  Assassin_ID | Target_ID |
|-----------|--------------|-----------|
"""

masterRows = [{1, 4320, "John", "Doe"}, {1, 4321, "John", "Doe2"},{1, 4322, "John", "Doe3"}]

gRows = [{1, 4320, "one", "two"}, {1, 4321, "two", "three"},{1, 4322, "three", "one"}]

# support for one game at a time to begin

def create_game():
    # Creates new database for
    return True

def get_game(gameID: int):
    # master database to keep record of all game
    return gRows

def add_participant(UID: int, assassinID: str):
    gRows.append({UID, assassinID, ""})



