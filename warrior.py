from chest import Chest

class Warrior(Chest):

    def __init__(self, name, lvl=1):
        self.name = name # warrior's name
        self.lvl = lvl # level
        if lvl <= 0:
            raise ValueError('error')
        elif lvl == 1:
            self.hp = 150 # health points
            self.strength = 20 # strength
            self.rs = 5 # running speed
        elif lvl == 2:
            self.hp = 300
            self.strength = 40
            self.rs = 6
        elif lvl == 3:
            self.hp = 500
            self.strength = 60
            self.rs = 7
        else:
            raise ValueError('error')
        self.gold = 0
        self.silver = 0
        self.copper = 0

    def armor(self, complect=1):
        self.complect = complect
        if complect == 1:
            self.hp = self.hp + 100
            self.ap = 100 # armor points
            self.rs = self.rs - 1
        elif complect == 2:
            self.hp = self.hp + 200
            self.ap = 200
            self.rs = self.rs - 2
        elif complect == 3:
            self.hp = self.hp + 300
            self.ap = 300
            self.rs = self.rs - 3
        else:
            raise ValueError('error')

    def sword(self, sword_name="rusty_sword"):
        self.sword_name = sword_name
        if sword_name == "rusty_sword":
            self.strength = self.strength + 5
        if sword_name == "silver_sword":
            self.strength = self.strength + 15
        else:
            raise ValueError('error')

    def shield(self, shield_name="broken_shield"):
        self.shield_name = shield_name
        if shield_name == "broken_shield":
            self.ap = self.ap + 10
        if shield_name == "wooden_shield":
            self.ap = self.ap + 25
        if shield_name == "iron_shield":
            self.ap = self.ap + 50

    def baff(self, skill):
        self.skill = skill
        if skill == "rage":
            self.hp = self.hp - 50
            self.strength = self.strength + 15
            self.rs = self.rs + 1
        elif skill == "windwalk":
            self.rs = self.rs + 3
        else:
            raise ValueError('error')

    def info(self):
        print("name: " + str(self.name))
        print("lvl: " + str(self.lvl))
        print("strength: " + str(self.strength))
        print("health: " + str(self.hp))
        print("armor: " + str(self.ap))
        print("speed: " + str(self.rs))

x = Warrior("Witcher", 2)
x.armor(2)
x.sword('silver_sword')
x.shield('iron_shield')
x.baff('windwalk')
x.info()
x.give_gold(10)
x.give_silver(35)
x.give_copper(140)
x.balance_info()

y = Warrior("Vesemir", 3)
y.armor(3)
y.sword('silver_sword')
y.shield('iron_shield')
y.baff('rage')
y.info()
y.give_gold(60)
y.give_silver(180)
y.give_copper(240)
y.balance_info()
