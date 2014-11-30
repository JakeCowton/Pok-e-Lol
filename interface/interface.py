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
		user_champion = raw_input("Which champion will you take? ")
		sys('clear')

		return int(user_champion)

	def ability_select(self, champion):

		print ""
		print "%s, which ability will you take? " % champion
		print ""
		print "Available abilities:"
		for key, ability in champion.abilities.iteritems():
			if ability.useable():
				print "%s - %s" % (key, ability)
		print "\n"
		ability = raw_input("Choose: Q, W, E or R - ")

		return ability.upper()

	def error(self, message):
		print message

	def attack(self, attacker, ability, atackee):
		sys('clear')
		print ""
		print "%s uses %s on %s" % (attacker, ability, atackee)

	def over_time(self, list_item):
		"""
		Says who is affected by what over time ability
		:type list_item: list
		:param list_item: A list item from AbilityManager.abilities_over_time
		"""
		ability, champion, turns_remaining = list_item
		print ""
		print "%s is damaged by %s for %d more turns" % \
			(champion, ability, turns_remaining)
		print ""
