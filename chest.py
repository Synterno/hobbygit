# Сундук с возможностью пополнения, снятия, обмена
# драгоценных металлов.


class Chest:

    def __init__(self, owner='Unknown adventurer'):
        self.gold = 0
        self.silver = 0
        self.copper = 0
        self.owner = owner

    def give_gold(self, count):
        self.gold = self.gold + count
        return count

    def take_away_gold(self, count):
        if self.gold - count < 0:
            raise ValueError('Нужно больше золота!')
        self.gold = self.gold - count
        return count

    def exchange_gold(self, silver, copper):
        if self.gold - (silver / 3 + copper / 6) < 0:
            raise  ValueError ('Нужно больше золота!')
        self.gold = self.gold - (silver / 3 + copper / 6)
        self.silver = silver
        self.copper = copper

    def give_silver(self, count):
        self.silver = self.silver + count
        return count

    def take_away_silver(self, count):
        if self.silver - count < 0:
            raise ValueError('Нужно больше серебра!')
        self.silver = self.silver - count
        return count

    def exchange_silver(self, gold, copper):
        if self.silver - (3 * gold + 3 / copper) < 0:
            raise ValueError('Нужно больше серебра!')
        self.silver = self.silver - (3 * gold + copper / 3)
        self.gold = gold
        self.copper = copper

    def give_copper(self, count):
        self.copper = self.copper + count
        return count

    def take_away_copper(self, count):
        if self.copper - count < 0:
            raise ValueError('Нужно больше медных монет!')
        self.copper = self.copper - count
        return count

    def exchange_copper(self, gold, silver):
        if self.copper - (6 * gold + 3 * silver) < 0:
            raise ValueError('Нужно больше медных монет!')
        self.copper = self.copper - (6 * gold + 3 * silver)
        self.gold = gold
        self.silver = silver

    def chest_balance(self):
        print(self.owner)
        print(self.gold)
        print(self.silver)
        print(self.copper)


a = Chest('Witcher')








