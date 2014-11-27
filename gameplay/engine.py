# engine.pys
from ability_manager import AbilityManager
from ..champion.ability import AbilityHeal, AbilityOverTime

class GameEngine(object):
	"""
	Manages the gameplay
	"""

	def __init__(self, interface, user, npc):

		self.interface = interface
		self.user = user
		self.npc = npc
		self.turn_count = 0
		self.ability_manager = AbilityManager(self.interface)

		self.run()

	def run(self):
		"""
		Creates a loop to run the game in
		"""
		while self.user.health > 0 and self.npc.health > 0:

			# Display game info e.g. health
			self.interface.display_info([self.user, self.npc])

			if self.turn_count % 2 == 0:
				# User
				self.user_turn(self.user)

			else:
				# NPC
				print "-----NPC does stuff-----"
				self.ability_manager.turn()
				self.npc_turn(self.npc)



	# User related functions
	def user_turn(self, champion):
		"""
		One turn
		@oaram champion The champion object whose turn it is
		"""
		# Select an ability
		ability = self.select_ability(champion)

		# Ability is activated

		# If ability is a heal, use on self
		if isinstance(ability, AbilityHeal):
			ability.use(champion)

		elif isinstance(ability, AbilityOverTime):
			# Add to the ability manager
			self.ability_manager.begin_over_time(ability, self.npc)
			# Use for first time
			ability.use(self.npc)

		# Otherwise, use on NPC
		else:
			ability.use(self.npc)
		self.interface.attack(champion, ability, self.npc)


		# Ability is put on cooldown
		self.ability_manager.put_on_cd(ability)


		self.turn_count += 1


	def select_ability(self, champion):
		"""
		Gets a champion to choose an ability to use
		@param champion Champion who will be choosing the ability
		"""
		choice = self.interface.ability_select(champion)

		if champion.abilities.has_key(choice):

			if champion.abilities.get(choice).useable():
				return champion.abilities.get(choice)
			else:
				self.interface.error("This ability is on cooldown")

		else:
			self.interface.error("This is not a valid ability")

		self.select_ability(champion)


	# NPC related functions
	def npc_turn(self, champion):
		# Do NPC stuff
		self.turn_count += 1