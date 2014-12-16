# champion.py
from ..fuzzy.membership_calculator import find_membership

class Champion(object):
	"""A class to define a champion"""

	def __init__(self, name, abilities, ocean):
		"""
		:type name: string
		:param name: The name of the champion
		:type abilities: dict {'Q': __, 'W':__, ...}
		:param abilities: The abilities the champion has
		:type ocean: dict {'O':__, 'C':__, ...}
		:param ocean: OCEAN score
		"""
		self.name = name
		self.health = 500
		# self.shield = 0
		self.set_abilities(abilities)
		self.ocean = ocean
		self.set_emotions()
		# A lower value means the NPC is less likely to do what
		# the neural networks says
	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def set_abilities(self, abilities):
		"""
		Sets the champions abilities
		:type abilities: dict {'Q': __, 'W':__, ...}
		:param abilities: The abilities the champion has
		"""
		self.abilities = dict(Q=abilities.get('Q'),
							  W=abilities.get('W'),
							  E=abilities.get('E'),
							  R=abilities.get('R'))

	def receive_heal(self, health):
		"""
		Champion has been given health
		"""
		self.health += health

	def receive_damage(self, damage):
		"""
		Champion has recieved damage
		"""

		self.health -= damage

		# # If the shield can take all the damage
		# if shield >= damage:
		# 	self.shield -= damage
		# 	# Remove the shield
		# 	shield = 0

		# # If the shield can take part of the damage
		# elif shield:
		# 	remaining = abs(shield - damage)
		# 	self.health -= remaining

		# # If there is no shield
		# else:
		# 	self.health -= damage

	def receive_shield(self, shield):
		"""
		Gives the champion a shield
		:type shield: integer
		:param shield: How much shield the champion gets
		"""
		self.shield += shield

	def set_emotions(self):
		"""
		Use emotions to calculate variables
		"""
		# Use a combination of whether O, C and A are high or low to determine
		# logic follows the majority of the 3 (O is inverse)
		from ipdb import set_trace; set_trace()
		logic_calc_inputs = [
			find_membership(self.ocean.get('O'), direct=False),
			find_membership(self.ocean.get('C')),
			find_membership(self.ocean.get('A'))
			]

		# Count occurences of high and low in logic_calc_inputs
		if logic_calc_inputs.count('HIGH') == 2:
			# Set logic at the highest value
			self.logic = 1.0
		elif logic_calc_inputs.count('LOW') == 2:
			# Set logic to the low value
			self.logic = 0.5
		else:
			raise ValueError

		# Calculate if `E` is high or low

		# N will cause the degradtion of L
			# If N is high: degradtion is fast
			# If N is low: degradtion is slow
