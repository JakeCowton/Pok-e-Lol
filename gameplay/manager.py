# Manages the gameplay
from ..environment.list_of_champions import ahri, kata


def start(user, npc):
	"""
	The main flow of the game
	@param user Champion object that the user will control
	@param npc Champion object that the computer will control
	"""
	print "%s is fighing %s" % (user, npc)
