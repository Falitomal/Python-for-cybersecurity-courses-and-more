# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 10:28:02 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 18:49:45 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
def reverse_msg():

	numberarg = len(sys.argv)
	words = sys.argv[1:]
	
	if numberarg < 2:
		print ()
		print ("Usage: python reverse_msg.py <message>")
	else:
		print (' '.join(words).swapcase())
	
reverse_msg()
