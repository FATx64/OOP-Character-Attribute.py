## Kelas,init,dict
class Hero:
	jumlah = 0

	def __init__(self, InputCategory, InputName, InputPower, InputUlti):
		#instance variable
		self.category = InputCategory
		self.name = InputName
		self.power = InputPower
		self.ulti = InputUlti
		Hero.jumlah =+ 1
		print ("Created Hero", InputName )

hero1 = Hero("Archer","Sasuke",300,"kirin")
hero2 = Hero("Saber","Naruto",200,"Rasengan")
hero3 = Hero("Tank","Gaara",250,"Pasir")

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
		