# engine.pys

class GameEngine(object):
	"""
	Manages the gameplay
	"""

	def __init__(self, interface, user, npc):

		self.interface = interface
		self.user = user
		self.npc = npc
		self.turn_count = 0

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
				self.npc_turn(self.npc)


	# User related functions
	def user_turn(self, champion):
		"""
		One turn
		@oaram champion The champion object whose turn it is
		"""
		ability = self.select_ability(champion)
		# Ability is activated
		# Ability is put on cooldown
		self.turn_count += 1

	def select_ability(self, champion):
		choice = self.interface.ability_select(champion)

		if champion.abilities.has_key(choice):
			ability = champion.abilities.get(choice)
		else:
			self.interface.error("This is not a valid ability")
			self.select_ability(champion)

		return ability

	# NPC related functions
	def npc_turn(self, champion):
		# Do NPC stuff
		self.turn_count += 1