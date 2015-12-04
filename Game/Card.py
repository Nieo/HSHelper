
class Card(object):
    """docstring for Card"""
    def __init__(self, arg):
        self.name = "cardname"
        self.id = "ID"
        self.cost = 0




class MinionCard(Card):
    """docstring for MinionCard"""
    def __init__(self, arg):
        super(MinionCard, self).__init__()
        self.attack = 0
        self.health = 0
        self.tribe = "none"

class SpellCard(Card):
    """docstring for SpellCard"""
    def __init__(self, arg):
        super(SpellCard, self).__init__()
        self.arg = arg

class WeaponCard(Card):
    """docstring for WeaponCard"""
    def __init__(self, arg):
        super(WeaponCard, self).__init__()
        self.arg = arg
        self.durability = 0
        self.attack = 0

