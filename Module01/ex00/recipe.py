# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:45:15 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 18:53:51 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys 

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None):
        """Constructor of the class Recipe"""
        if validate_args(name, cooking_lvl, cooking_time, ingredients, recipe_type, description):
            self.name = name
            self.cooking_1v1= cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.recipe_type = recipe_type
            self.description = description
        else:
            print("Invalid arguments")
            exit()
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        return "Recipe name: " + self.name + "\nCooking level: " + str(self.cooking_lvl) + "\nCooking time: " + str(self.cooking_time) + "\nIngredients: " + str(self.ingredients) +  "\nRecipe type: " + self.recipe_type + "\nDescription: " + self.description

def validate_args(name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None):
    """Check if the arguments are valid"""
    if type(name) is not str or len(name) == 0:
        return False
    if type(cooking_lvl) is not int or cooking_lvl < 1 or cooking_lvl > 5:
        return False
    if type(cooking_time) is not int or cooking_time <= 0:
        return False
    if type(ingredients) is not list or len(ingredients) == 0:
        return False
    if type(recipe_type) is not str or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert") or len(recipe_type) == 0:
        return False
    if type(description) is not str or len(description) == 0:
        return False
    return True