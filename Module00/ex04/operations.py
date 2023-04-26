# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 11:18:22 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 12:18:34 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def operations(nbr):
    if len(nbr) > 3:
        print("AssertionError: numbers incorrects arguments")
        exit()
    elif len(nbr) <= 2:
        print("AssertionError: numbers incorrects arguments")
        print("Usage:\n python operations.py <number1> <number2>")
        print("Example:\n python operations.py 4 2")
        exit()

    try:
        nbr1 = int(nbr[1])
        nbr2 = int(nbr[2])
    except ValueError:
        print("AssertionError: only integers")
        exit()
    nbr1 = int(nbr[1])
    nbr2 = int(nbr[2])
        
    print(f"Sum:	{nbr1 + nbr2} ")
    print(f"Difference:{nbr1 - nbr2} ")
    print(f"Product: {nbr1 * nbr2} ")
    if nbr2 == 0:
        print("ERROR (division by zero)")
    else:
        print(f"Quotient: {nbr1 / nbr2} ")
    if nbr2 == 0:
        print("ERROR (modulo by zero)")
    else:
        print(f"Remainder: {nbr1 % nbr2} ")

if __name__=="__main__":
    operations(sys.argv)