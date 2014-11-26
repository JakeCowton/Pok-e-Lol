# Ability definitions for:
# Ability_Q
# Ability_W_Damage
# Ability_E_Heal
# Ability_R_Attack


class Ability(object):
    """A class to outline abilities"""

    def __init__(self, name, cooldown):
        """
        @param name Name of the ability
        @param cooldown How many turns ability is on cooldown
        """
        self.name = name
        self.cooldown = cooldown

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def useable(self):
        # Check if the ability is on cooldown
        if cooldown == 0: return True
        else: return False


class Ability_Q(Ability):
    """
    This deals raw damage
    """

    def __init__(self, name, cooldown, damage):
        """
        @param damage how much damage the attack does
        """
        Ability.__init__(self, name, cooldown)
        self.damage = damage

    def use(self, champion):
        """
        @param champion the champion the attack is being used on
        """
        Ability.use(self)
        champion.receive_damage(self.damage)


class Ability_W(Ability):
    """
    A class to outline a W ability
    These are `over time` abilities
    """

    def __init__(self, name, cooldown, turns):
        Ability.__init__(self, name, cooldown)
        self.turns = turns


class Ability_W_Damage(Ability_W):
    """
    This deals damage x over the next y turns
    """

    def __init__(self, name, cooldown, turns, damage):
        Ability_W.__init__(self, name, cooldown, turns)
        self.damage = damage


# class Ability_W_Buff(Ability_W):
#     """
#     This gives a damage buff for x turns
#     """

#     def __init__(self, name, cooldown, turns, multiplyer):
#         Ability_W.__init__(self, name, cooldown, turns)
#         self.multiplyer = multiplyer


class Ability_E_Heal(Ability):
    """
    This heals a champion
    """

    def __init__(self, name, cooldown, health):
        Ability.__init__(self, name, cooldown)
        self.health = health

    def heal(self, champion):
        champion.heal(self.health)


# class Ability_E_Shield(Ability):
#     """
#     This creates a shield which absorbs x damage from the next attack
#     """

#     def __init__(self, name, cooldown, shield):
#         Ability.__init__(self, name, cooldown)
#         self.shield = shield

#     def shield(self, champion):
#         champion.shield(self.shield)
#         return True


# class Ability_R_Buff(Ability):
#     """
#     This creates a damage multipler for the next x turns
#     """

#     def __init__(self, name, cooldown, turns, multiplyer):
#         Ability.__init__(self, name, cooldown)
#         self.turns = turns
#         self.multiplyer = multiplyer


class Ability_R_Attack(Ability_Q):
    """
    This deals heavy raw damage
    """

    def __init__(self, name, cooldown, damage):
        Ability_Q.__init__(self, name, cooldown, damage)
