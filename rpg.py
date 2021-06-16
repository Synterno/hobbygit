# MAIN of warrior.py mobs.py chest.py mechanics.py

from warrior import Warrior
from mobs import Orc, Dragon
from chest import Chest

x = Warrior("Thorin", 2)
x.armor(2)
x.sword('silver_sword')
x.shield('wooden_shield')
x.baff('windwalk')
x.give_gold(10)
x.give_silver(35)
x.give_copper(140)
x.info()

z = Orc('Azog', 3)
z.armor(2)
z.sword('silver_sword')
z.baff('rage')
z.give_copper(40)
z.info()

w = Dragon('Smaug', 3)
w.armor(3)
w.give_gold(9999)
w.info()



