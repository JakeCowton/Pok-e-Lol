# Interface for the game

class Interface(object):

	def introduction(self):
		print ""
		print "Welcome to Pok-e-LoL"
		print "A total rip-off of pokemon and League of Legends"
		print ""

	def display_info(self, champions):
		for champion in champions:
			print "%s has %d HP" % (champion, champion.health)
		print "\n"


	def champion_select(self, champions):

		print "Available Champions:"
		for i in range(len(champions)):
			print "%d - %s" % (i, champions[i])
		print "\n"
		user_champion = raw_input("Which champion will you take? ")

		return int(user_champion)

	def ability_select(self, champion):

		print ""
		print "%s, which ability will you take? " % champion
		print ""
		print "Available abilities:"
		for key, ability in champion.abilities.iteritems():
			print "%s - %s" % (key, ability)
		print "\n"
		ability = raw_input("Choose: Q, W, E or R - ")

		return ability.upper()

	def error(self, message):
		print message