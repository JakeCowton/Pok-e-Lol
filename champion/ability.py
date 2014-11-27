# Ability definitions


class Ability(object):
    """A class to outline abilities"""

    def __init__(self, name, cooldown):
        """
        @param name Name of the ability
        @param cooldown How many turns ability is on cooldown
        """
        self.name = name
        self.cooldown = cooldown
        self.on_cd = False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def useable(self):
        """
        Check if the ability is on cooldown
        """
        if not self.on_cd: return True
        else: return False



class AbilityRawDamage(Ability):
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
        champion.receive_damage(self.damage)


class AbilityOverTime(Ability):
    """
    Deals damage over time
    """

    def __init__(self, name, cooldown, turns, damage):
        Ability.__init__(self, name, cooldown)
        self.turns = turns
        self.damage = damage

    def use(self, champion):
        # This will be executed `self.turns` times
        champion.receive_damage(self.damage)


class AbilityHeal(Ability):
    """
    This heals a champion
    """

    def __init__(self, name, cooldown, health):
        Ability.__init__(self, name, cooldown)
        self.health = health

    def use(self, champion):
        champion.receive_heal(self.health)
