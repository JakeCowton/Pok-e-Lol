# ability_manager.py

class AbilityManager(object):
	"""
	Manages ability cooldowns and damage over time
	"""
	# [[ability, champion, turns_remaining]...]
	abilities_over_time = []
	# [[ability, turns_remaining]...]
	abilities_on_cd = []

	def __init__(self, interface):
		"""
		@param interface The interface used for outputing data
		"""
		self.interface = interface

	def turn(self):
		"""
		What needs to be done each turn
		"""

		# Manager over time abilities
		queue_for_ot_removal = []
		for i in range(len(self.abilities_over_time)):

			# If he over time ability is on the last turn
			if self.abilities_over_time[i][2] == 1:
				# Use the attack once more
				self.abilities_over_time[i][0].use(self.abilities_over_time[i][1])
				# Queue for removal after iteration complete
				queue_for_ot_removal.append(self.abilities_over_time[i])

			else:
				# Use the attack
				self.abilities_over_time[i][0].use(self.abilities_over_time[i][1])
				# Reduce the number of turns
				self.abilities_over_time[i][2] -= 1

			# Display that the attack was done
			self.interface.over_time(self.abilities_over_time[i])

		# Remove the abilities queued for removal
		for ability in queue_for_ot_removal:
			self.end_over_times(ability)


		# Manage cooldowns
		queue_for_cd_removal = []
		for i in range(len(self.abilities_on_cd)):

			# If the ability is due to end cooldown period
			if self.abilities_on_cd[i][1] == 1:
				# Queue for removal after iteration
				queue_for_cd_removal.append(self.abilities_on_cd[i])
			else:
				# Decrease the amount of time left on cooldown
				self.abilities_on_cd[i][1] -= 1

		# Remove the abilities queued for removal
		for ability in queue_for_cd_removal:
			self.take_off_cd(ability)


	# Cooldown specific functions
	def put_on_cd(self, ability):
		"""
		Put an ability on cooldown
		@param ability Ability object
		"""
		# Add it to the list of abilties on cooldown
		self.abilities_on_cd.append([ability, ability.cooldown + 1])
		# Set the ability as `on_cd`
		ability.on_cd = True

	def take_off_cd(self, ability):
		"""
		Take an ability off cooldown
		@param ability Ability object
		"""
		# Take the ability off cooldown
		self.abilities_on_cd.remove(ability)
		# Set the ability as not on_cd
		ability[0].on_cd = False


	# Over time specific functions
	def begin_over_time(self, ability, champion):
		# Add to the over time list
		# turns - 1 as 1 hit has already been dealt
		self.abilities_over_time.append([ability, champion, (ability.turns - 1)])

	def end_over_times(self, ability):
		# Stop the ability from do its over time affects
		self.abilities_over_time.remove(ability)