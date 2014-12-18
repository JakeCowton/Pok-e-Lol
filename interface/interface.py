# Interface for the game
from os import system as sys

class Interface(object):

	def introduction(self):
		print ""
		print "Welcome to Pok-e-LoL"
		print "A total rip-off of pokemon and League of Legends"
		print ""

	def display_info(self, champions):
		print "\n"
		for champion in champions:
			print "%s has %d HP" % (champion, champion.health)
		print "\n"


	def champion_select(self, champions):

		print "Available Champions:"
		for i in range(len(champions)):
			print "%d - %s" % (i, champions[i])
		print "\n"
		user_champion = None

		while not user_champion:
			user_champion = raw_input("Which champion will you take? ")
			if not int(user_champion) < len(champions):
				print "Invalid choice"
				user_champion = None

		sys('clear')

		return int(user_champion)

	def ability_select(self, champion):

		print ""
		print "%s, which ability will you take? " % champion
		print ""
		print "Available abilities:"

		for key, ability in champion.get_available_abilities().iteritems():
			print "%s - %s" % (key, ability)

		print ""

		ability = None
		while not ability:
			ability = raw_input("Choose: ")
			if not champion.get_available_abilities().has_key(ability.upper()):
				ability = None

		sys('clear')

		return ability.upper()

	def error(self, message):
		print message

	def attack(self, attacker, ability, atackee):
		print ""
		try:
			# Show the damage dealt
			print "%s uses %s on %s - %d damage" % (attacker, ability, atackee, ability.damage)
		except AttributeError:
			# These will be heals as they have no damage
			print "%s uses %s on %s" % (attacker, ability, atackee)

	def defend(self, defender, ability):
		print ""
		print "%s uses %s - %d health" % (defender, ability, ability.health)

	def over_time(self, list_item):
		"""
		Says who is affected by what over time ability
		:type list_item: list
		:param list_item: A list item from AbilityManager.abilities_over_time
		"""
		ability, receiver, turns_remaining, giver = list_item
		print ""
		print "%s is still damaged by %s's %s  - %d damage" % \
			(receiver, giver, ability, ability.damage)
		print ""

	def game_over(self, user, npc):
		"""
		Someone has died
		:type user: Champion()
		:param user: The user object
		:type npc: Champion()
		:param npc: The npc object
		"""
		sys('clear')
		print "The game is over"
		# set any sub zero healths to 0
		if user.health <= 0:
			user.health = 0
		if npc.health <=0:
			npc.health = 0
		print "The user has %d health" % user.health
		print "The npc has %d health" % npc.health
