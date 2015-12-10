"""
Provide a main function
Use if __name__ == '__main__': to run this function from the command line. 
The main function should call your two functions in order, passing your 
list of preferences to the drink creation function. It should then print 
out the contents of the drink.
^^what does this mean?

"""
import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

inventory = {
	"glug of rum":1, "slug of whisky":1, "splash of gin":1,
    "olive on a stick":1, "salt-dusted rim":1, "rasher of bacon":1,
    "shake of bitters":1, "splash of tonic":1, "twist of lemon peel":1,
    "sugar cube":1, "spoonful of honey":1, "spash of cola":1,
    "slice of orange":1, "dash of cassis":1, "cherry on top":1,
}

name_part1 = ['asdf', 'bnm,', 'cvbn', 'dfgh']

name_part2 = ['1', '2', '3', '4']


def ask_questions():
	print("answer with 'y' or 'yes' for yes, and anything else for no")
	order_dictionary = {}
	for element in questions:
		answer = input((questions[element])+"\n> ")
		if answer=='y' or answer=='yes':
			order_dictionary[element]=True
		else:
			order_dictionary[element]=False
	return order_dictionary

def create_drink(order):
	drink = []
	for taste in order:
		if order[taste]:
			ingredient = random.choice(ingredients[taste]) #a
			if check_inventory(ingredient):
				drink.append(ingredient)
			else:
				available_ingredient = find_available_ingredient(taste)
				if available_ingredient==False:
					print("unfortunately we can't make you a "+taste+" drink")
					another_drink()
				else:
					print('unfortunately we are out of '+ingredient)
					print('but we can use '+available_ingredient)				
					drink.append(available_ingredient)
	return drink

def check_inventory(ingredient):
	inventory[ingredient] -= 1
	return inventory[ingredient]>=0

def find_available_ingredient(taste):
	for item in ingredients[taste]:
		if check_inventory(item):
			return item
	return False 

def get_drunk():
	patrons_drink = create_drink(ask_questions())
	drink_name = str(random.choice(name_part1[0]))+" "+str(random.choice(name_part2[0]))
	print('here is your drink '+str(patrons_drink))
	print('it is called a '+str(drink_name))
	another_drink()

def another_drink():
	another = input('do you want another? y/n\n> ')
	if another=='y':
		get_drunk()
	else:
		decision=False

get_drunk()





