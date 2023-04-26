# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 16:10:30 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 13:27:45 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

def ft_progress(lst):
    lensize = len(lst)
    start_time = time.time()
    etatime = 0
    for i, index in enumerate(lst):
        elapsed_time = time.time() - start_time
        percent_complete = (i + 1) * 100 / lensize
        filled_slots = int (percent_complete / 5)
        empty_slots = 20 - filled_slots
        etatime = (elapsed_time / (percent_complete / 100.0))
        
        progress = "[" + "=" * filled_slots + ">" + " " * empty_slots + "]"

        sys.stdout.write("\r ETA: {:.2f}s [{:0.2f}%] {} ({}/{}) | elapsed time {:.2f}s".format(etatime, percent_complete, progress, i+1, lensize, elapsed_time))
        sys.stdout.flush()
        yield index

if __name__ == "__main__":
    lst = range(100)
    retu = 0
    for element in ft_progress(lst):
        retu += element
        time.sleep(0.005)
    print()
    print("...")
    print(retu)