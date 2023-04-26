# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 16:11:15 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 13:24:46 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse_txt = {
    "A": ".-",    "B": "-...",    "C": "-.-.",    "D": "-..",    "E": ".",
    "F": "..-.",    "G": "--.",    "H": "....",    "I": "..",    "J": ".---",
    "K": "-.-",    "L": ".-..",    "M": "--",    "N": "-.",    "Ñ": "--.--",
    "O": "---",    "P": ".--.",    "Q": "--.-",    "R": ".-.",    "S": "...",
    "T": "-",    "U": "..-",    "V": "...-",    "W": ".--",    "X": "-..-",
    "Y": "-.--",    "Z": "--..",    "0": "-----",    "1": ".----",    "2": "..---",
    "3": "...--",    "4": "....-",    "5": ".....",    "6": "-....",
    "7": "--...",    "8": "---..",    "9": "----.",    ".": ".-.-.-",
    ",": "--..--",    ":": "---...",    "?": "..--..",    "'": ".----.",
    "-": "-....-",    "/": "-..-.",    "\"": ".-..-.",    "@": ".--.-.",
    "=": "-...-",    "!": "−.−.−−",
}

txt_plane = " ".join(sys.argv[1:])
morse = ""
words = txt_plane.split()
for i, word in enumerate(words):
    for char in word.upper():
        if char in morse_txt:
            morse += morse_txt[char] + ' '
        else:
            print("ERROR")
            exit()
    
    if i < len(words) - 1:
        morse += '/ ' 
    else:
        morse += ''
print(morse)





