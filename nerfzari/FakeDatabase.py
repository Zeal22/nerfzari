from typing import List, Any


# Temporary until records database completely set.
# Master database

"""
Game ID |    UID    |  F_name |  L_name |
--------|-----------|---------|---------|
"""

# per game database
"""
Game ID |    UID    |  Assassin_ID | Target_ID |
--------|-----------|--------------|-----------|
"""

masterDB = [{1, 4320, "John", "Doe"}, {1, 4321, "John", "Doe2"},{1, 4322, "John", "Doe3"}]

gamedb = [{1, 4320, "one", "two"}, {1, 4321, "two", "three"},{1, 4322, "three", "one"}]

def add_game(object: 'Game') -> int:
	games.append(object)
	return len(games)-1

def get_game(game_id: int) -> 'Game':
	return games[game_id]
