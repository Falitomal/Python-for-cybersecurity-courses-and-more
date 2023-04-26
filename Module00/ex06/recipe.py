# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:52:38 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 16:18:30 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system



cookbook = {
"Sandwich":{
"ingredents":["Ham", "Bread", "cheese", "tomatoes"],
"meal":"lunch",
"takes":10,
},
"Cake":{
"ingredents":["flour", "sugar", "eggs"],
"meal":"dessert",
"takes":60,
},
"Salad":{
"ingredents":["avocado", "arugula", "tomatoes", "spinach"],
"meal":"lunch",
"takes":15,
}
}

def show_menu():
		system("clear")
		print("Welcome to the Python Cookbook !")
		print("List of available options:")
		print(f"1. Add recipe")
		print(f"2. Delete a recipe")
		print(f"3. Print a recipe")
		print(f"4. Print the cookbook")
		print(f"5. Quit\n")


def print_recipe(name_recipe):
	if name_recipe in cookbook:
		recipe = cookbook[name_recipe]
		print(f"Recipe for {name_recipe}")
		print(f"\t Ingredients list: {recipe['ingredents']}")
		print(f"\t To be eaten for: {recipe['meal']}")
		print(f"\t Takes {recipe['takes']} minutes of cooking")
		print("")
	else:
		print(f"Recipe {name_recipe} not found in cookbook")

def delete_recipe(name_recipe):
	if name_recipe in cookbook:
		del cookbook[name_recipe]
		print(f"Recipe {name_recipe} deleted")
	else:
		print(f"Recipe {name_recipe} not found in cookbook")

def print_cookbook():
	for name_recipe in cookbook:
		print(name_recipe)

def add_recipe():
	name_recipe = input("Enter the name of the recipe: ")
	recipe = {}
	empty_line = 0
	list_ingredents = []
	while empty_line < 1:
		word = input("Enter the ingredents of the recipe : ")
		if word == "":
			empty_line =+1
		else:
			list_ingredents.append(word)
	recipe["ingredents"] = list_ingredents
	recipe["meal"] = input("Enter the type of meal : ")
	number= input("Enter the preparation time : ")
	if number.isnumeric():
		recipe["takes"] = number
	else:
		return(print("Only integer"))
	cookbook[name_recipe] = recipe
	print(f"Recipe {name_recipe} added to cookbook")



show_menu()
while True:
	option = input("Select an option: ")
	if option == '1':
		add_recipe()
	elif option == '2':
		print("Name recipe to delete")
		nameRecipe = input()
		delete_recipe(nameRecipe)
	elif option == '3':
		print("Name recipe to print")
		nameRecipe = input()
		print_recipe(nameRecipe)		
	elif option == '4':
		print_cookbook()
	elif option == '5':
		exit()