# champion.py
from ability import Ability_Q, __Ability_W, \
				   Ability_E_Heal, Ability_E_Shield, \
				   Ability_R_Buff, Ability_R_Attack

class Champion(object):
	"""A class to define a champion"""

	def __init__(self, name, stats, abilities):
		"""
		@param name The name of the champion
		@param stats dict The stats the champion has
		@param abilities dict The abilities the champion has
		"""
		self.name = name
		self.health = stats.get('health')
		self.attack = stats.get('attack')
		self.armour = stats.get('armour')
		self.agility = stats.get('agility')
		self.shield = 0

	def set_abilities(self, abilities):
		"""
		Sets the champions abilities
		@param abilities dict The abilities the champion has
		"""
		# Check the Q ability is valid
		if isinstance(abilities.get('Q'), Ability_Q):
			self.Q = abilities.get('Q')
		else:
			raise ValueError("%s is not a valid Q abilty") % \
				str(abilities.get('Q'))

		# Check the W ability is valud
		if isinstance(abilities.get('W'), Ability_W):
			self.W = abilities.get('W')
		else:
			raise ValueError("%s is not a valid W abilty") % \
				str(abilities.get('W'))

		# Check the E ability
		if isinstance(abilities.get('E'), Ability_E_Heal) or \
			isinstance(abilities.get('E'), Ability_E_Shield):
			self.E = abilities.get('E')
		else:
			raise ValueError("%s is not a valid E abilty") % \
				str(abilities.get('E'))

		# Check the R ability
		if isinstance(abilities.get('R'), Ability_R_Buff) or \
			isinstance(abilities.get('R'), Ability_E_Attack):
			self.E = abilities.get('R')
		else:
			raise ValueError("%s is not a valid R abilty") % \
				str(abilities.get('R'))

	def receive_heal(self, health):
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

	def receive_shield(self, shield):
		"""
		Gives the champion a shield
		@param shield How much shield the champion gets
		"""
		self.shield += shield
