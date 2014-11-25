# champion.py
from ability import Ability_Q, \
					Ability_W_Damage, \
				    Ability_E_Heal, \
				    Ability_R_Attack

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

		# Check the Q ability is valid
		if isinstance(abilities.get('Q'), Ability_Q):
			self.abilities['Q'] = abilities.get('Q')
		else:
			raise ValueError("Invalid Q ability")

		# Check the W ability is valud
		if isinstance(abilities.get('W'), Ability_W_Damage):
			self.abilities['W'] = abilities.get('W')
		else:
			raise ValueError("Invalid W ability")

		# Check the E ability
		if isinstance(abilities.get('E'), Ability_E_Heal):
			self.abilities['E'] = abilities.get('E')
		else:
			raise ValueError("Invalid E ability")

		# Check the R ability
		if isinstance(abilities.get('R'), Ability_R_Attack):
			self.abilities['R'] = abilities.get('R')
		else:
			raise ValueError("Invalid R ability")

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

	def use_ability_Q(self, champion):
		"""
		@param champion The champion the ability is being used on
		"""
		self.Q.use(champion)

	def use_ability_W(self, champion):
		"""
		@param champion The champion the ability is being used on
		"""
		self.W.use(champion)

	def use_ability_E(self, champion):
		"""
		@param champion The champion the ability is being used on
		"""
		self.E.use(champion)

	def use_ability_R(self, champion):
		"""
		@param champion The champion the ability is being used on
		"""
		self.R.use(champion)
