# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:45:18 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 18:04:08 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            print("The name must be a string")
            exit()
        self.name = name
        self.last_update = datetime.now()
        self.create_date = datetime.now()
        self.recipe_list = {"starter": [], "lunch": [], "dessert": []}
    
    def get_recipe_by_name(self, name):
        """Search recipe by name and print it"""
        for recipe_type in self.recipe_list:
            for recipe in self.recipe_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"Recipe not found: {name}")
        return
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipe_list.keys():
            print("Invalid arguments, recipe type must be starter, lunch or dessert")
            return 
        for recipe in self.recipe_list[recipe_type]:
            print(recipe.name)
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Invalid recipe")
            return
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_upd = datetime.now()
        print(f"\nRecipe added ¨{recipe.name}¨ to the book {self.name}")
        
    def __str__(self):
        """Return the string to print with the recipe info"""
        str =   f'Name: {self.name}\n' \
                f'Last update: {self.last_update}\n' \
                f'Creation date: {self.create_date}\n' \
                f'Recipes: {self.recipe_list}'
        return str