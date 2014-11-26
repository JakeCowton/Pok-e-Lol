# Interface for the game

class Interface(object):

	def champion_select(self, champions):

		print "Available Champions:"
		for i in range(len(champions)):
			print "%d - %s" % (i, champions[i])
		print "\n"
		user_champion = raw_input("User, which champion will you take? ")

		return int(user_champion)
