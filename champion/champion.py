# champion.py

class Champion(object):
	"""A class to define a champion"""

	def __init__(self, name, abilities, ocean=None):
		"""
		:type name: string
		:param name: The name of the champion
		:type abilities: dict {'Q': __, 'W':__, ...}
		:param abilities: The abilities the champion has
		:type ocean: dic {'O':__, 'C':__, ...}
		:param ocean: OCEAN score
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
