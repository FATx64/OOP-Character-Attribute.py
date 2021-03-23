class Hero:
	jumlah = 0

	def __init__(self, InputName, InputPower, InputHealth, InputCrit):
		self.name = InputName
		self.power = InputPower
		self.health = InputHealth
		self.crit = InputCrit

	def who(self):
		print("my name is", self.name)

	def getHealth(self):
		return self.health

def div():
		print("----------------------------------------------------------------")

	
hero1 = Hero("Traveler",1000,1200,200)
hero2 = Hero("Klee",3000,2330,124)

hero1.who()
print("health = ", hero1.getHealth())
print(hero1.__dict__)
div()
hero2.who()
print("health = ",hero2.getHealth())
print(hero2.__dict__)
