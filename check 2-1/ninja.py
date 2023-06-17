from fighter import Fighter
from exc import Exceptiki

class Ninja(Fighter, Exceptiki):
    def __init__(self):
        super(Ninja, self).__init__()
        self.attackername = Exceptiki.nam(self) # Применение класса исключений
        self.attackercoming = "I'm as free as the dust in the solar wind"



