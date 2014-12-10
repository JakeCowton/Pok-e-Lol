from ..environment import training_data

class NPC(object):
	""" Controls the NPCs actions """

	def __init__(self, champion):
		data = None
		self.champion = champion
		if champion.name.upper() == 'AHRI':
			self.name = 'Ahri'
			data = training_data.get_ahri()
		# Get the nerual networked trained to the champion
		self.nn = create_nn(self.data)

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def attack_or_defend(self):
		"""
		Use the SLP to calculate whether to attack or defenc
		"""

	def choose_attack(self):
		pass

	def choose_defence(self):
		pass