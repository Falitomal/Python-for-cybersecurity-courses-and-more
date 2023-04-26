# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 10:27:55 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 13:20:17 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
def whois():
	if (len(sys.argv) != 2):
		print("AssertionError: argument incorret are provided")
		print("Usage:\n python whois.py <number>")
		exit()
	try:
		args = sys.argv[1]
		nmb = int(args)
	except:
		print("AssertionError: argument is not an integer")
		print("Usage:\n python whois.py <number>")
		exit()
	if (nmb == 0):
		print("I'm Zero.")
	elif (nmb % 2 == 0):
		print("I'm Even.")
	elif (nmb % 2 == 1):
		print("I'm Odd.")
whois()