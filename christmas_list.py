import sys, os

def get_name():
	name = raw_input("Please enter your name: ").lower()
	return name

file_name = ""

def create_christmas_list():
	name = get_name()
	file_name = "{0}_christmas_list.txt".format(name)
	if os.path.isfile(file_name):
		print "Hello, {0}, welcome to your christmas list.\nYour file, {1}, is already found".format(name, file_name)
		return file_name
	else:
		f = open(file_name, "w")
		print "Hello, {0}, welcome to your christmas list.\nIt will be saved in {0}_christmas_list.txt".format(name)
		f.write("{0}'s Christmas List:\n".format(name))
		f.close()
		return file_name

presents = []

file_name = create_christmas_list()

choice = raw_input("What would you like to do with your christmas list\nWould you like to:\n1)Read List\n2)Add Present\n3)Delete Present\n4)Delete List\nPlease enter the number corresponding to the options: ")
if choice == 2:
	f = open(file_name, "r")
	f.read()
	f.close()
elif choice == 2:
	pres = p.add_present()

class Present:

	def __init__(self, name, price, url):
		self.name = name
		self.price = price
		self.url = url

	def add_present(self):
		f = os.path.realpath(file_name)
		fl = open(f, "a")
		fl.writelines(self.details() + '\n')
		fl.close()
		return "Your present has been added to the list."

	def details(self):
		return "Name: {0}\nPrice: ${1}\nUrl/Location: {2}".format(self.name, self.price, self.url)

def create_present():
		n = raw_input("Please enter the name of the gift: ")
		p = raw_input("Please enter the price of: {0}. $".format(n))
		u = raw_input("Please enter the url/location to purchase: {0}. ".format(n))
		temp_present = Present(n, p, u)
		presents.append(temp_present)
		return temp_present


p = create_present()
p.add_present()
#print p.details()