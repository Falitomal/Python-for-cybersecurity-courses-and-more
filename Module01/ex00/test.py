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

if __name__ == "__main__":
    
    my_book = Book("My test book")
    tortilla = Recipe("Tortilla", 1, 10, ["eggs", "potatoes", "onion"], "the best tortilla from mlg", "lunch")
    campero = Recipe("Campero", 1, 10, ["chicken", "mayonesa", "bread"], "the best burger from mlg", "dinner")
    my_book.add_recipe(campero)
    my_book.add_recipe(campero)
    
    print(my_book.get_recipe_by_name("Campero"))
    print(my_book.get_recipes_by_types("dinner"))
    
    
    