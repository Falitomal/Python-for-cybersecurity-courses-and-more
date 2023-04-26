# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 10:27:32 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 19:59:49 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def text_analyzer(myText = ""):
    """ text_analyzer that takes a single string argument and displays the sums
    of its upper-case characters, lower-case characters, punctuation characters and spaces."""
    if not isinstance(myText, str):
        print("AssertionError: argument is not a string")
        print("Usage: python count.py <text>")
        return()
    if myText == "":
        myText = input("What is the text to analyze? \n")
    letterUp = 0
    letterlow = 0
    puntuchar = 0
    spaces = 0
    for letter in myText:
        if letter.isupper():
            letterUp += 1
        elif letter.isspace():
            spaces += 1
        elif letter.islower():
            letterlow += 1
        elif letter.isascii() and not letter.isnumeric():
            puntuchar += 1
    print(f"The text contains {len(myText)} character(s): \n")
    print(f"- {letterUp} upper letter(s)")
    print(f"- {letterlow} lower letter(s)")
    print(f"- {puntuchar} punctuation mark(s)")
    print(f"- {spaces} space(s)")
		

if __name__=="__main__": 
    if len(sys.argv) > 2:
        print("more than one argument")
    elif len(sys.argv) < 2:
        text_analyzer("")
    else:
    	text_analyzer(sys.argv[1])