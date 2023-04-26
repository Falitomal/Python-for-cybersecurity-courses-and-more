# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 12:56:20 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 12:33:23 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
'PHP': 'Rasmus Lerdorf',
}

for name, values in kata.items():
    print(f"{name} was created by {values}")