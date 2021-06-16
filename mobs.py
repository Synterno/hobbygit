# part of rpg.py
from warrior import Warrior
from chest import Chest

class Orc(Warrior):

	def __init__(self, name, lvl=1):
		Warrior.__init__(self, name, lvl)
		self.hp = self.hp + 100
		self.strength = self.strength + 20
		self.rs = self.rs + 4

	def armor(self, complect=1):
		Warrior.armor(self, complect)
		self.ap = self.ap + 50

	def drop(self):
		self.copper = copper

class Dragon(Warrior):

	def __init__(self, name, lvl=1):
		Warrior.__init__(self, name, lvl)
		self.hp = self.hp + 300
		self.strength = self.strength + 100
		self.rs = self.rs + 15

	def armor(self, complect=1):
		Warrior.armor(self, complect)
		self.ap = self.ap + 150

	def drop(self):
		self.gold = gold

