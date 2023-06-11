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
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        """Constructor of the class Recipe
        Args: name, cooking_lvl, cooking_time, ingredients, recipe_type, description
        we check if the arguments are valid"""

        if not isinstance(name, str):
            print("The name must be a string")
            exit()
        self.name = name
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            print("The cooking level must be an integer between 1 and 5 inclusive")
            exit()
        self.cooking_lvl = cooking_lvl
        if not isinstance(cooking_time, int) or cooking_time <= 0:
            print("The cooking time must be a positive integer")
            exit()
        self.cooking_time = cooking_time
        if not isinstance(ingredients, list) or len(ingredients) == 0 or not all(isinstance(x, str) for x in ingredients):
            print("The ingredients must be a non-empty list of strings")
            exit()
        self.ingredients = ingredients
        if not isinstance(description, str):
            print("The description must be a string")
            exit()
        self.description = description
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("Invalid arguments, recipe type must be starter, lunch or dessert")
            exit()
        self.recipe_type = recipe_type
    print("Recipe added")

    def __str__(self):
        """Return the string to print with the recipe info"""
        str =   f'Name: {self.name}\n' \
                f'Cooking level: {self.cooking_lvl}\n' \
                f'Cooking time: {self.cooking_time} mins\n' \
                f'Ingredients: {self.ingredients}\n' \
                f'Recipe type: {self.recipe_type}\n' \
                f'Description: {self.description}'
        return str
    
