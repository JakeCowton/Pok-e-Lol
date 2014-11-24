# champion.py

class Champion(object):
	"""A class to define a champion"""

	def __init__(self, name, health, attack, armour, agility):
		self.name = name
		self.health = health
		self.attack = attack
		self.armour = armour
		self.agility = agility
		self.shield = 0

	def heal(self, health):
		"""
		Champion has been given health
		"""
		self.health += health

	def receive_damage(self, damage):
		"""
		Champion has recieved damage
		"""
		# If the shield can take all the damage
		if shield >= damage:
			self.shield -= damage
			# Remove the shield
			shield = 0

		# If the shield can take part of the damage
		elif shield:
			remaining = abs(shield - damage)
			self.health -= remaining

		# If there is no shield
		else:
			self.health -= damage

	def shield(self, shield):
		self.shield += shield
