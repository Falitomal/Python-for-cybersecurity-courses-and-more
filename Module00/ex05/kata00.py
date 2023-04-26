# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 12:50:21 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 12:33:07 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
def printNum():
	kata = (19,42,21)
	print(f"The {len(kata)} numbers are:", end='')
	print(*kata, sep=',')
printNum()