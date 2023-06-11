# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:46:30 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 17:46:31 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import itertools
import random

def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        yield "ERROR"
        return

    words = text.split(sep)

    if option == "shuffle":
        indices = list(range(len(words)))
        random.shuffle(indices)
        words = [words[i] for i in indices]

    elif option == "unique":
        words = list(dict.fromkeys(words))

    elif option == "ordered":
        words.sort()

    elif option is not None:
        yield "ERROR"
        return

    for word in words:
        yield word


