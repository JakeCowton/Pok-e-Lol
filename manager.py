# Manages the gameplay
from numpy.random import randint
from environment.list_of_champions import champions
from interface.interface import Interface
from gameplay.engine import GameEngine

def champion_select(interface):
    """
    Get the user to select a champion
    """
    index = interface.champion_select(champions)

    try:

        return champions.pop(index)

    except IndexError:
        print "This champion does not exist. Choose another."
        champion_select(interface)


def main():
    """
    Script to run the game
    """


    interface = Interface()

    interface.introduction()

    user = champion_select(interface)

    if len(champions) == 1:
        npc = champions.pop()

    else:
        npc = champions.pop(randint(0, (len(champions)-1)))

    engine = GameEngine(interface, user, npc)


if __name__ == '__main__':
    main()
