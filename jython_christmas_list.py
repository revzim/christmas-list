import sys, os
import javax.swing.JOptionPane.showInputDialog as sid
import javax.swing.JOptionPane.showMessageDialog as smd
def get_name():
	name = sid("Please enter your name: ").lower()
	return name

file_name = ""

def create_christmas_list():
	name = get_name()
	file_name = "{0}_christmas_list.txt".format(name)
	if os.path.isfile(file_name):
		smd(None, "\nHello, {0}, welcome to your christmas list.\n\nYour file, {1}, is already found".format(name, file_name))
		return file_name
	else:
		f = open(file_name, "w")
		smd(None, "\nHello, {0}, welcome to your christmas list.\n\nIt will be saved in {0}_christmas_list.txt".format(name))
		f.write("{0}'s Christmas List:\n".format(name))
		f.close()
		return file_name

presents = []

file_name = create_christmas_list()


class Present:

	def __init__(self, name, price, url):
		self.name = name
		self.price = price
		self.url = url

	def add_present(self):
		f = os.path.realpath(file_name)
		fl = open(f, "a")
		fl.write('\n' + self.details())
		fl.close()
		smd(None, "Your present has been added to the list.")


	def details(self):
		return "\nName: {0}\nPrice: ${1}\nUrl/Location: {2}\n".format(self.name, self.price, self.url)

def create_present():
		n = sid("Please enter the name of the gift:")
		p = sid("Please enter the price of: {0}.".format(n))
		u = sid("Please enter the url/location to purchase: {0}.".format(n))
		temp_present = Present(n, p, u)
		presents.append(temp_present)
		return temp_present

c = sid("\nWhat would you like to do with your christmas list?\n\nWould you like to:\n\t1)Read List\n\t2)Add Present\n\t3)Delete List\n\nPlease enter the number corresponding to the options: ")
c = int(c)
if c == 1:
	f = open(file_name, "r")
	smd(None, f.read())
	f.close()
elif c == 2:
	p = create_present()
	pres = p.add_present()
elif c == 3:
	ans = sid("\nAre you sure you want to delete your Christmas list? Enter either 'y/n': ")
	if ans == "y":
		os.remove(os.path.realpath(file_name))
		smd(None, "\nYour Christmas List has been deleted.")
	else:
		smd(None, "\nGood Choice! Try to get as many options on the list as possible.")
else:
		smd(None, "\nSorry you are not reading instructions. Please try to run the program again and read the instructions this time.")

