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

import sys
from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        self.name = name
        self.last_upd = datetime.now()
        self.create_date = self.last_upd
        self.recipe_list = {"starter": [], "lunch": [], "dessert": []}
    
    def __str__(self):
        return "Book name: " + self.name + "List ingredents: " + self.recipe_list + "Last update: " + self.last_upd + "Creation date: " + self.create_date  
    
    def get_recipe_by_name(self, name):
        for recipe in self.recipe_list:
            if recipe.name == name:
                print(recipe)
                return recipe
        print("Recipe not found")
        return None
    
    def get_recipes_by_types(self, recipe_type):
        for recipe in self.recipe_list:
            if recipe.recipe_type == recipe_type:
                print(recipe)
        return None
    
    def add_recipe(self, recipe):
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_upd = datetime.now()
        print("Recipe added")
        return None
        