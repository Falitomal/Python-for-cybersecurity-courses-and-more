# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 13:18:09 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 12:38:24 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (2019, 9, 25, 3, 30)
from datetime import datetime
datetipe = datetime(kata[0], kata[1], kata[2],kata[3], kata[4])
data_obj = datetipe.strftime('%m/%d/%y %H:%M')
print(data_obj)