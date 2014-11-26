# ability_manager.py

class AbilityManager(object):
	"""
	Manages ability cooldowns and damage over time
	"""
	abilities_on_cd = []

	def turn(self):

		# Instigate any damage over time

		# Manage cooldowns
		queue_for_removal = []
		for i in range(len(self.abilities_on_cd)):

			if self.abilities_on_cd[i][1] == 1:
				queue_for_removal.append(self.abilities_on_cd[i])
			else:
				self.abilities_on_cd[i][1] -= 1

		for ability in queue_for_removal:
			self.take_off_cd(ability)


	def put_on_cd(self, ability):
		"""
		Put an ability on cooldown
		@param ability Ability object
		"""
		self.abilities_on_cd.append([ability, ability.cooldown])
		ability.on_cd = True

	def take_off_cd(self, ability):
		"""
		Take an ability off cooldown
		@param ability Ability object
		"""
		ability[0].on_cd = False
		self.abilities_on_cd.remove(ability)