# To practice object oriented python, we are going to create a tool to manage a building.
# We will need a command line interface for our tool. On the command line, we should be able to
# create buildings, units in those buildings, and people to occupy the buildings.

# We should also be able (at any time) to view occupants in any floor in any building. Remember to keep your
# code DRY and to practice the OOP methodology (public classes, private classes, static methods, class methods).

# This exercise will be done alone but that doesn't mean you should never talk to anybody.
# This exercise will also be done in Python.
import random

building_list = []

class Building(object):

	# constructor
	def __init__(self, name, number, street): 
		self.name = name 
		self.number = number
		self.street = street
		self.stories = 0
		self.units = {} 
		self.unit_count = 0 

	def add_unit(self, unit_object):
		self.unit_count = self.unit_count + 1		
		self.units[unit_object.number] = unit_object
		print "Unit", unit_object.number, "added to", self.name, "on floor", unit_object.floor," Total units now: ", self.unit_count
		if (unit_object.floor > self.stories): 
			self.stories = unit_object.floor
			print "Number of stories = ", self.stories 

	def total_occupancy(self):
		return unit_count

	def total_revenue(self): 
		return		

	# returns the street address, the total number of units filled, the total revenue
	# and the businesses inside 
	def building_status(self):
		print self.name,"is", self.stories,"stories tall and has a total of",self.unit_count,"units"
		print self.units[222].get_occupants()
		# for number in self.units:
		# 	print self.units[number].get_occupants()



# class Floor(object):
# 	def__init__(self, floor):


# 	def add_unit(self, unit_object):
# 		pass

# 	def view_occupants(self):
# 		0list = []
# 		for number in self.units: 
# 			# olist.append(self.units[number].get_occupants())
# 			unit = self.units[number]
# 			unit_occupents = unit.get_occupants()
# 			olist.append(unit_occupents)
# 			return olist


class Unit(object):
	def __init__(self, number, maxOccupancy, rent, floor, occupied):
		self.number = number
		self.maxOccupancy = maxOccupancy
		self.rent = rent
		self.occupied = 0  
		self.floor = floor 
		self.tenant = None 

	# moves an occupant into a unit
	def move_in(self, tenant_object):
		# self.tenants[tenant_object.name] = tenant_object
		print "Added tenant", tenant_object.name, "to unit number", self.number 
		self.tenant = tenant_object
		self.occupied = 1
		return

	# moves an occupant out of a unit
	def move_out(self):
		print "Moving tenant", self.tenant.name, "from unit", self.number, "confirmed."
		# self.tenants.clear() was originally used when the tenant was modeled with a dictionary
		self.tenant = None
		self.occupied = 0 
		print "Tenants status is now:  " + str(unit340.tenant) 

	# returns whether the unit is filled, the occupant, the business, and if the rent is current. 
	def get_occupants(self):
		return self.tenant.name

	# returns whether the unit is filled, the occupant, the business, and if the rent is current. 
	def get_status(self):
		tenant_report = "Tenant name: " + self.tenant.name + ", specializing in, " + self.tenant.business
		return tenant_report



class Tenant(object):
	def __init__(self, name, business, rent_current):
		self.name = name
		self.business = business
		self.rentCurrent = rent_current

	def tenant_details(self):
		return 



# Conner's code
# my_unit = Unit()
# first_building.view_occupants(3)



# Building Manager Code



buildingOne = Building("Hawthorn Manor", 113, "Mockingbird Lane")
buildingTwo = Building("The Stanton", 10, "Pronto Street")

print "Building One:", buildingOne.name, "at", buildingOne.number, buildingOne.street
print "Building Two:", buildingTwo.name, "at", buildingTwo.number, buildingTwo.street



# creating units
unit123 = Unit(123, 7, 1000, 1, 0)
unit222 = Unit(222, 13, 20000, 2, 0)
unit317 = Unit(317, 20, 45000, 3, 0)
unit320 = Unit(320, 20, 46000, 3, 0)
unit340 = Unit(340, 20, 46000, 3, 0)
unit100 = Unit(100, 5, 100, 1, 0)


# adding a unit to a building 
buildingOne.add_unit(unit123)
buildingOne.add_unit(unit222)
buildingOne.add_unit(unit317)
buildingOne.add_unit(unit320)
buildingOne.add_unit(unit340)
buildingOne.add_unit(unit100)


# creating tenants 
tenantOne = Tenant("Jefferson", "Dentistry", 1)
tenantTwo = Tenant("Madison", "Dentistry", 1)
tenantThree = Tenant("Wilson", "Podiatry", 1)
tenantFour = Tenant("Lincoln", "Proctology", 1)

# adding tenants to units
unit222.move_in(tenantOne)
unit340.move_in(tenantTwo)
unit317.move_in(tenantFour)


# interrogating units for tenants
print "Interrogate unit 222: ", unit222.get_status()
print "Interrogate unit 340: ", unit340.get_status()
print "Interrogate unit 317: ", unit317.get_status()



# interrogating building one 
buildingOne.building_status()

print "Units:  " + str(buildingOne.units)
print "Tenants:  " + str(unit340.tenant) 
print "Moveout "

unit340.move_out() # THIS DOESN'T WORK 

print "dir ", str(dir(unit340))
print "Tenants:  " + str(unit340.tenant) 

print "Unit Count  " + str(buildingOne.unit_count)



# # Client code
# name = raw_input("Which building to search? ")
# floor = int(raw_input('which floor')
# b = buldings[name]
# b.view_occupants(floor)


# ***********************************************************
# *************** Interface Starts Here *********************
# ***********************************************************

command_input = ""

while (command_input != "q"):

	command_input = raw_input("What would you like to do? -- Type 'h' for help commands 'q' to quit:  " )

	if (command_input == "h"):
		print "nb for new building"
		print "nf for new floor"
		print "nu for new unit" 
		print "nt for new tenant"
		print "i interrogate"
		print "h prints this message"
		print "q to quit"
	elif command_input == 'nb':
		command_input1 = "Please enter a building name "
		command_input2 = "Please enter a street number "
		command_input3 = "Please enter a street name "
		building_list.append(Building(command_input1, command_input2, command_input3))



# Questions
# How do you create new building names? 


