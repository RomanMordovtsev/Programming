from fighter import Fighter
from exc import Exceptiki

class Karateboy(Fighter, Exceptiki):
    def __init__(self):
        super(Karateboy, self).__init__()
        self.defendername = Exceptiki.nam(self) # Применение класса исключений
        self.defendercoming = "Alalalalallallalalalalalalalalllalala"



