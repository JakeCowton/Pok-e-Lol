# ability.py


class __Ability(object):
    """A class to outline abilities"""

    def __init__(self, name, cooldown):
        """
        @param name Name of the ability
        @param cooldown How many turns ability is on cooldown
        """
        self.name = name
        self.cooldown = cooldown

    def useable(self):
        if cooldown == 0: return True
        else: return False

    def use(self):
        self.cd_timer = self.cooldown

    def turn(self):
        if self.cd_timer > 0:
            self.cd_timer -= 1


class Ability_Q(__Ability):
    """
    This deals raw damage
    """

    def __init__(self, name, cooldown, damage):
        __Ability.__init__(self, name, cooldown)
        self.damage = damage

    def use(self):
        Ability.use(self)
        champion.receive_damage(self.damage)


class __Ability_W(__Ability):
    """
    A class to outline a W ability
    These are `over time` abilities
    """

    def __init__(self, name, cooldown, turns):
        __Ability.__init__(self, name, cooldown)
        self.turns = turns


class Ability_W_Damage(__Ability_W):
    """
    This deals damage x over the next y turns
    """

    def __init__(self,name, cooldown, turns, damage):
        __Ability_W.__init__(self, name, cooldown, turns)
        self.damage = damage


class Ability_W_Buff(__Ability_W):
    """
    This gives a damage buff for x turns
    """

    def __init__(self,name, cooldown, turns, multiplyer):
        __Ability_W.__init__(self, name, cooldown, turns)
        self.multiplyer = multiplyer



class Ability_E_Heal(__Ability):
    """
    This heals a champion
    """

    def __init__(self, name, cooldown, health):
        __Ability.__init__(self, name, cooldown)
        self.health = health

    def heal(self, champion):
        champion.heal(self.health)
        return True


class Ability_E_Shield(__Ability):
    """
    This creates a shield which absorbs x damage from the next attack
    """

    def __init__(self, name, cooldown, shield):
        __Ability.__init__(self, name, cooldown)
        self.shield = shield

    def shield(self, champion):
        champion.shield(self.shield)
        return True


class Ability_R_Buff(__Ability):
    """
    This creates a damage multipler for the next x turns
    """

    def __init__(self, name, cooldown, turns, multiplyer):
        __Ability.__init__(self, name, cooldown)
        self.turns = turns
        self.multiplyer = multiplyer


class Ability_R_Attack(Ability_Q):
    """
    This deals raw damage
    """

    def __init__(self, name, cooldown, damage):
        Ability_Q.__init__(self, name, cooldown, damage)