#   shield = 0
#   def __init__(self, shield):
#      self.shield = shield
# issubclass(Plasmodium, Unit)

class Unit:
	def __init__(self, armor, damage, hp, name):
		self.armor = armor
		self.damage = damage
		self.hp = hp
		self.maxHP = hp
		self.name = name
		#self.endurance = endurance
		#self.energy = energy
		#self.attackers = attackers
	
	def findTarget(self, targetsList):
		return targetsList[0]
		##TODO
		
		
	def attack(self):
		target = findTarget()
		##self.attackers.append(Marto)
		print "%s attacks %s" % (self.name, target.name)
		target.takeDamage(self.damage)

	def checkIfDead (self, hp, name):
		if not hp > 0:
			print "%s died" % (self.name)
			targetsList.remove(self)
		
	def takeDamage (self, damage):
		print "%s taking damage" % (self.name)    ###TODO %s is taking damage from %s
		self.hp -= damage - self.armor
		self.checkIfDead(self.hp, self.name)
	
	def __str__(self):
		return "%s: A:%d HP:%d" % (self.name, self.armor, self.hp)
		
class Bio():
	pass
	
class Mech():
	pass
	
class Armored():
	pass
		


		
		
		
		
		
class Plasmodiums(Unit):
	def demotivation(self, target):
		print "demotivating %s" % (target.name)

class Plasmodium(Plasmodiums):
	a = 0
	def __init__(self):
	
		Plasmodium.a += 1
		name = "Plasmodium_" + str(Plasmodium.a)
		Unit.__init__(self, 1, 50, 20, name)




class HappyGreenPirates(Unit):
	def motivating():
		print "motivating"
	
class GreenPirate(HappyGreenPirates):
	a = 0
	def __init__(self):
	
		GreenPirate.a += 1
		name = "Pirate_" + str(GreenPirate.a)
		Unit.__init__(self, 1, 50, 125, name)


		
		
class ScorpionMans(Unit):
	pass

class Scorpion(ScorpionMans):
	a = 0
	def __init__(self):
		
		Scorpion.a += 1
		name = "Scorpion_" + str(Scorpion.a)
		Unit.__init__(self, 1, 50, 125, name)
		

class Toshkoids(Unit):
	def destruktivAura():
		print "destrukting"
	
class Toshkoid(Toshkoids):
	a = 0
	def __init__(self):
		
		Toshkoid.a += 1
		name = "Toshkoid_" + str(Toshkoid.a)
		Unit.__init__(self, 1, 50, 125, name)
		
class Electrones(Unit):
	a = 0
	def __init__(self, shield):
	
		self.shield = shield
		
		Electrone.a += 1
		name = "Electrone_" + str(Electrone.a)
		Unit.__init__(self, 1, 50, 125, name)
		
	def takeDamage (self, damage):
		if self.shield > 0:
			self.shield -= damage - self.armor
			if self.shield < 0:
				self.hp += self.shield
		self.shield = 0

class Electrone():
	a = 0
	def __init__(self):
		
		Electrone.a += 1
		name = "Electrone_" + str(Electrone.a)
		Unit.__init__(self, 1, 50, 125, name)

class Furries(Unit):
	pass

class Khajiit(Furries):
	a = 0
	def __init__(self):
		
		Khajiit.a += 1
		name = "Khajiit_" + str(Khajiit.a)
		Unit.__init__(self, 1, 50, 125, name)

class Illuminats(Unit):
	a = 0
	def __init__(self):
		
		Illuminats.a += 1
		name = "Illuminat_" + str(Illuminats.a)
		Unit.__init__(self, 1, 50, 125, name)

if __name__ == "__main__":

	targetsList = []
	attackersList = []

	
	Pavkata = Plasmodium()
	Marto = GreenPirate()
	Aleks = Scorpion()
	Aleks1 = Scorpion()

	targetsList.append(Marto)	
	targetsList.append(Marto)	
	targetsList.append(Marto)	
	attackersList.append(Aleks)
	attackersList.append(Pavkata)
	attackersList.append(Aleks1)
	
	print Aleks
	print Aleks1
	print Pavkata
	print Marto
	
	a = 0
	for a in range(len(attackersList)):
		attackersList[a].attack(targetsList[a])
	
	print targetsList
