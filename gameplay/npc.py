
from numpy import array
from ..environment import training_data
from ..ann.nn_manager import create_nn, call_nn

class NPCManager(object):
	""" Controls the NPCs actions """

	def __init__(self, npc, user):
		# Store vars
		data = None
		self.npc = npc
		self.user = user

		data = None
		# Get training data
		if npc.name.upper() == 'AHRI':
			self.name = 'Ahri'
			data = training_data.get_ahri()

		# Get the nerual networked trained to the npc
		self.nn = create_nn(data)

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def attack_or_defend(self):
		"""
		Use the SLP to calculate whether to attack or defenc
		"""
		pass

	def choose_attack(self):
		"""
		Use the NN to choose an attack
		:rtpye: char
		:returns: The attack ability to use
		"""
		inputs = array([
			float(self.user.health),
			float(self.npc.abilities['R'].damage),
			float(self.npc.abilities['R'].useable()),
			float(self.npc.abilities['W'].damage),
			float(self.npc.abilities['W'].useable()),
			float(self.npc.abilities['Q'].damage)
		 ])
		outputs = call_nn(self.nn, inputs)
		# Emotional stuff here
		choice = None, None
		if outputs[0] > choice[1]:
			choice = 'R', outputs[0]
		if outputs[1] > choice[1]:
			choice = 'W', outputs[1]
		if outputs[2] > choice[1]:
			choice = 'Q', outputs[2]

		return choice[0]

	def choose_defence(self):
		pass