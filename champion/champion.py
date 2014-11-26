# champion.py

class Champion(object):
	"""A class to define a champion"""

	def __init__(self, name, abilities, ocean=None):
		"""
		@param name The name of the champion
		@param abilities dict The abilities the champion has
		@param ocean dict OCEAN score
		"""
		self.name = name
		self.health = 500
		# self.shield = 0
		self.set_abilities(abilities)

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def set_abilities(self, abilities):
		"""
		Sets the champions abilities
		@param abilities dict The abilities the champion has
		"""
		self.abilities = dict()

		# Set the Q ability
		self.abilities['Q'] = abilities.get('Q')

		# Set the W ability
		self.abilities['W'] = abilities.get('W')

		# Set the E ability
		self.abilities['E'] = abilities.get('E')

		# Set the R ability
		self.abilities['R'] = abilities.get('R')

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
		@param shield How much shield the champion gets
		"""
		self.shield += shield
