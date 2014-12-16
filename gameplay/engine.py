# engine.pys

from numpy.random import choice
from ability_manager import AbilityManager
from ..champion.ability import AbilityHeal, AbilityOverTime
from .npc import NPCManager

class GameEngine(object):
    """
    Manages the gameplay
    """

    def __init__(self, interface, user, npc):

        self.interface = interface
        self.user = user
        self.npc = npc
        self.npc_manager = NPCManager(self.npc, self.user)
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
                self.npc_turn(self.npc)

                # Do the ability_management stuff
                self.ability_manager.turn()

        self.interface.game_over(user=self.user, npc=self.npc)


    # User related functions
    def user_turn(self, champion):
        """
        One turn for a user
        :type champion: Champion object
        :param champion: The champion object whose turn it is
        """
        # Select an ability
        ability = None
        while not ability:
            ability = self.select_ability(champion)

        # Ability is activated

        # If ability is a heal, use on self
        if isinstance(ability, AbilityHeal):
            ability.use(champion)

        elif isinstance(ability, AbilityOverTime):
            # Add to the ability manager
            self.ability_manager.begin_over_time(ability, self.npc, self.user)
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
        :type champion: Champion object
        :param champion Champion who will be choosing the ability
        """
        choice = self.interface.ability_select(champion)

        if champion.abilities.has_key(choice):

            if champion.abilities.get(choice).useable():
                return champion.abilities.get(choice)
            else:
                self.interface.error("This ability is on cooldown")

        else:
            self.interface.error("This is not a valid ability")


    # NPC related functions
    def npc_turn(self, champion):
        """
        One turn for an NPC
        :type champion: Champion object
        :param champion: The champion whose turn it is
        """
        # Choose dttack or defend
        # avr_dmg_given, avr_dmg_taken = self.calc_stats_for_slp()
        a_or_d = self.npc_manager.attack_or_defend([self.npc.health,
                                                    self.user.health
                                                    ])
        ability = None
        # If NPC is not an extrovert use the NN to choose ability
        if self.npc.extroversion.upper() is 'LOW':
            while not ability:

                if a_or_d.upper() == 'ATTACK':
                    ability = self.npc_manager.choose_attack()
                elif a_or_d.upper() == 'DEFEND':
                    ability = self.npc_manager.choose_defence()
                    if not ability:
                        ability = self.npc_manager.choose_attack()
                else:
                    raise KeyError


                if not self.npc.abilities.has_key(ability) or \
                  not self.npc.abilities.get(ability).useable():
                    ability = None
                else:
                    ability = self.npc.abilities.get(ability)

        # If they are an extrovert, take a random ability
        else:
            # Choose a random ability from the list of available abilities
            available_abilities = self.npc.get_available_abilities()
            ability = available_abilities.get(choice(available_abilities.keys()))


        # If ability is a heal, use on self
        if isinstance(ability, AbilityHeal):
            ability.use(champion)

        # If ability is an over time use on user and add to m
        elif isinstance(ability, AbilityOverTime):
            # Add to the ability manager
            self.ability_manager.begin_over_time(ability, self.user, self.npc)
            # Use for first time
            ability.use(self.user)

        # Otherwise, use on user
        else:
            ability.use(self.user)

        # Print what the attack used
        self.interface.attack(champion, ability, self.user)

        # Ability is put on cooldown
        self.ability_manager.put_on_cd(ability)

        # Increment the turn counter
        self.turn_count += 1

    # def calc_stats_for_slp(self):
    #     npc_avr_damage_given = float((500 - self.user.health) / self.turn_count)
    #     npc_avr_damage_taken = float((500 - self.npc.health) / self.turn_count)

    #     return npc_avr_damage_given, npc_avr_damage_taken

