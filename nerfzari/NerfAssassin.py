from datetime import datetime
from typing import List,Any
import User
from Game import Game,GameType

class NerfAssassin(Game):

	GAME_TYPE = GameType.NERF_ASSASSIN
	TYPE_NAME = "Nerf Assassin"
	participants: List['User']

	def __init__(self, name: str, start_date: datetime):
		super().__init__(self.GAME_TYPE)
		self.name = name
		self.start_date = start_date
		self.id = 0
		self.participants = []
	# -------------------------------------------------------------------------

	def __str__(self):
		return str(self.id) + " - " + self.TYPE_NAME + " - " + self.name + " - " + str(self.start_date)

	# -------------------------------------------------------------------------

	def leaderboard(self):
		"""
		:returns: True if leaderboard is successfully printed; otherwise False is returned.
		"""
		print("--- " + str(self) + " ---")
		for index,participant in enumerate(self.participants):
			print(str(index+1) + " - " + str(participant))
		return True
	# -------------------------------------------------------------------------

	def status(self, handle: str):
		"""
		:param handle: handle of the participant to print the status of (is_alive, current target, # kills... etc)
		:return: True if status has been successfully retrieved and printed; otherwise False is returned.
		"""
		participant = self.get_participant(handle)
		if participant is None:
			print("ERROR: Assassin " + participant + " is not a participant in " + self.name)
			return False

		msg = "Name: "
		msg += participant.first_name
		msg += " "
		msg += participant.last_name
		msg += " Handle: "
		msg += participant.handle
		msg += " Kills "
		msg += str(len(participant.kills))
		msg += " Target: "
		msg += participant.target

		print(msg)
		return True
	# -------------------------------------------------------------------------

	def register_kill(self, assassin_handle: str, assassinated_handle: str):
		"""
		:param assassin_handle: Handle of the assassin that performed the kill
		:param assassinated_handle: Handle of the participant that was assassinated
		:param game_id: Unique id of the game the assassination was performed under
		:return: True if the kill was successfully registered; otherwise False is returned.
		"""

		assassin = self.get_participant(assassin_handle)
		if assassin is None:
			print("ERROR: Assassin " + assassin_handle + " is not a participant in " + self.name)
			return False
		assassinated = self.get_participant(assassinated_handle)
		if assassinated is None:
			print("ERROR: Assassin " + assassinated_handle + " is not a participant in " + self.name)
			return False

		assassin.kills.append(assassinated_handle)
		assassinated.is_alive = False
		assassinated.deaths += 1
		assassinated.assassinator = assassin_handle

		return True
	# -------------------------------------------------------------------------

	def add_participant(self, user: User):
		"""
		:param user: Name of the user to add
		:param game_id: Unique id of the game to add the user to
		:return: True if user has been successfully added to the game; otherwise False is returned.
		"""
		self.participants.append(user)

		return True
	# -------------------------------------------------------------------------

	def get_participant(self, handle) -> User:
		"""
		:param handle: The handle of the participant to retrieve
		:return: User object of the participant; otherwise None is returned
		"""
		participant: str

		for user in self.participants[:]:
			if user.handle == handle:
				participant = user
		return participant
	# -------------------------------------------------------------------------

	def distribute_targets(self):
		"""
		:return: True if all participants were assigned a target; otherwise False is returned.
		"""

		raise NotImplementedError()
	# -------------------------------------------------------------------------
