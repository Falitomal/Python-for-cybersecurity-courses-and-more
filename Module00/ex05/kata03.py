# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 14:29:42 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 12:39:32 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = "The right format"
lenstr = len(kata)
for i in range(42-lenstr):
	print("-", end="")
print(kata,end="")