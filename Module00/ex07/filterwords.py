# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 18:58:42 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 19:51:03 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) != 3:
    print("Error")
    exit()

s = sys.argv[1]
n = sys.argv[2]

if not isinstance(s, str):
    print("Error: s must be a string")
    exit()
try:
    size = int(n)
except ValueError:
    print("Error")
    exit()

if size < 0:
    print("Error: n must be positive")
    exit()
translator = str.maketrans('', '', string.punctuation)
s = s.translate(translator)

words = s.split()
words = [word for word in words if len(word) > size]

print(words)