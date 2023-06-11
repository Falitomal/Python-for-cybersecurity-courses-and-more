# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:45:36 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 17:45:37 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    """A class representing the Game of Thrones character"""
    def __init__(self, first_name, is_alive=True):
        """Initiate the character"""
        if not isinstance(first_name, str):
            print("The name must be a string")
            exit()
        if not isinstance(is_alive, bool):
            print("The is_alive must be a boolean")
            exit()
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        """Initiate the Stark"""
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Print the house words"""
        print(self.house_words)
    
    def die(self):
        """Set is_alive to False"""
        self.is_alive = False
        