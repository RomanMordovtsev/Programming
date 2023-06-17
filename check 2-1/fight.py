from ninja import Ninja
from karate import Karateboy
from spemix import SpeechMixin
import random

class Fight(Ninja, Karateboy, SpeechMixin):
    def __init__(self):
        super(Fight, self).__init__()
        self.health = [self.health, self.health]
        self.hairstyle = SpeechMixin.hairstyle(self)

    @property
    def check(self):
        if not 0 in self.health:
            return True
        else:
            return False

    def sadness(self): # Реализация исключения для внезапной смены погоды
        try:
            if random.randint(0, 5) == 2:
                raise Exception('Rain')
        except Exception:
            print('It started raining') # Реализация возбуждения исключения, т.е. возвращение сигнала об испорченной погоде
    @property
    def fight(self):
        while self.check:
            i = random.randint(0, 1)

            if i + 1 == 1:
                fighter1 = self.attackername
                print(self.attackercoming)
                fighter2 = self.defendername
            else:
                fighter1 = self.defendername
                print(self.defendercoming)
                fighter2 = self.attackername
            try: # Создание поддержки исключений
                self.health[i] -= 20
                print(fighter1, 'hits', fighter2)
                print(self.health[i], "Loser's HP left")
            except self.health[i] <= 0:
                print(fighter1, 'kills', fighter2)

        if random.randint(0, 2) == 1:
            self.sadness()
        return self.hairstyle

    @property
    def dance(self):
        return 'Winner Dances (Use Your Imagination)'
