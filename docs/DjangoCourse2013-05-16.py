woof = ["Greyhound", "breakfast", "walk", "lunch"]
doggie = woof[:] # recommended way to shallow copy a list

#raw string
here = r"Osney Mead\nOxford" #the \n is not interpreted as a new line
here = "Osney Mead\\nOxford" #The equivalent when escaping \n
print here

year = 2012

# Functions within if conditional blocks
if year > 2012:
	def retirementTime(age):
		return 67 - age

def retirementTime(age):
	# This will print year
	print "Running for year", year
	# I can only read the variable defined outside it's scope but not modify it 
	year = year + 1
	return 67 - age


class book (object):
	def __init__(current,name,author,pubyear):
		# It doesn't have to be self. It can be any variable name. Common ones are current, self and this
		current.pubyear = pubyear
		current.title = name	#Can use different variable names
		current._author = author #_ indicates an understanding it is private
		pass

	def expireCopyright(self):
		#The variable name can change for each method
		return self.pubyear+75

	def setPubyear(self, year):
		self.pubyear = year

	def getPubyear(self):
		return self.pubyear

	def setauthor(self, author):
		self.author = author

	def getauthor(self):
		return self.author

	def __str__(this):
		#Overriding what gets printed when printing this class
		return '"'+this.title+'"'

	author = property(getauthor, setauthor)
	author = property(getauthor, None) # Cannot change the author here.
	# The above methos is like method dandruff. Defining classes which have just one line. We can use lambda instead
	author = property(lambda x:x._author, None) # Cannot change the author here

class periodical1(book):
	#Class periodical is based on the book. For the moment it is exactly the same as a book
	pass

class periodical(book):
	#Class periodical is based on the book. It extends the class book
	def expireCopyright(self):
		#The variable name can change for each method
		return self.pubyear+15

if name == __main__:
	nineteen = book("1984","George Orwell",1948)
	doom = book("Harry potter and the temple of doom","J K Rowling",2007)
	rovers = periodical1("Coronation street Journal","Cast of a 100",2011)

	yoe = nineteen.expireCopyright()
	print nineteen,"is out of copyright in",yoe

	yoe = rovers.expireCopyright()
	print rovers,"is out of copyright in",yoe
	print rovers.title # can be done. Still prefers get and set methods
	print rovers._author #it will work but this is not fair game
	print rovers.author #this will work as we have defined the property for author

# When importing would prefer import rather than from so that the namespaces are maintained
import transport as t #This is better way.
from transport import * #Bad practise

def soccer(noOFPeople):
	#Return number of teams. 15 people per team
	return noOFPeople / 15

staff = (600,50,7,250000)

marathon = lambda x: x - 5

def mymap(action,source):
	result = []
	for item in source:
		result.append(action(item))
	return result

staffSoccerTeams = map(soccer,staff)
print staffSoccerTeams

scrabble = map(lambda x: x/2, staff) # return number of teams, two per team
print scrabble

runners = map(marathon, staff)
print runners

scrabble = mymap(lambda x: x/2, staff) # return number of teams, two per team
print scrabble

bod = 789
bodrunners = marathon(bod)
print bodrunners

stuff = {"Oxfordshire":"Oxford", "Berkshire":"Reading", "Wiltshire":"Trowbridge"}
stuff["Oxfordshire"] = "Kindlington"
for county in stuff.keys():
	print "The county town of", county, "is", stuff[county]

def bynamelength(dis, dat):
	return len(dis) - len(dat)


try:
	stuff["Hertfordshire"] += "Town"
except StandardError, e:
	stuff["Hertfordshire"] = "Hertford"
	print e.message
	print e.__class__.__name__


def getTown(which):
	fh = open("filename")
	gotted = []
	for lyne in fh.readlines(): #list of 90000 items
		if lyne.find(which) >= 0:
			gotted.append(lyne)
			print "yum"
	return gotted
co = 0
for hit in getTown("Trowbridge"):
	co += 1
	print co,hit

def getTownSmart(which):
	fh = open("filename")
	for lyne in fh.xreadlines(): #generator for readlines
		if lyne.find(which) >= 0:
			print "yum"
			yield lyne

def getTownSmart(which):
	for lyne in open("filename"): #generator for readlines - same as xreadlines
		if lyne.find(which) >= 0:
			print "yum"
			yield lyne

#If in doubt use a generator

a = [10]
b = [10]
a =c
a == b 
 # True
a is b
 # False
a is c
 # True

a = 10
b = 10
a == b
 # True
a is b
 # True

