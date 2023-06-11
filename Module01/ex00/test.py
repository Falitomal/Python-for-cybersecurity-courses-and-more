# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:45:13 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 19:04:54 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

# My test recipe book

jl = Recipe("Tarta ReedVelvet", 4, 280,["Mantequilla", "Queso", "Harina", "Azucar", "Huevos"], "dessert", "Tarta de queso tipo red velvet mmmm")

jl2 = Recipe("Tarta de manzana", 3, 120,["Mantequilla", "Manzana", "Harina", "Azucar", "Huevos"], "dessert", "Tarta de manzanita hambre")
jl3 = Recipe("Tarta de Vacia", 2, 20,["Mantequilla",  "Harina", "Azucar", "Huevos"], "dessert", "")
print(jl)
print(jl2)
print(jl3)

# My test book
print("My test book\n")
my_book = Book("My recipe book")
print("\n")
my_book.add_recipe(jl)
my_book.add_recipe(jl2)
print("OBtenemos tarata manza\n")

my_book.get_recipe_by_name("Tarta de manzana")
print("Postres\n")
my_book.get_recipes_by_types("dessert")
print("\n")
print(my_book.last_update)
print("Tipos")
my_book.get_recipes_by_types("dessert")
print("\nTipo vacio")
my_book.get_recipes_by_types("lunch")