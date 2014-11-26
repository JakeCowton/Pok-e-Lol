# Manages the gameplay
from ..environment.list_of_champions import champions
from ..interface.interface import Interface

def champion_select(interface):
	"""
	Get the user to select a champion
	"""
	index = interface.champion_select(champions)

	try:
		return champions[index]

	except IndexError:
		print "This champion does not exist. Choose another."
		champion_select(interface)


def main():
	interface = Interface()
	user = champion_select(interface)

if __name__ == '__main__':
	main()
