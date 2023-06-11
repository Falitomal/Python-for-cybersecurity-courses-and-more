# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:47:06 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 17:47:07 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Definimos una clase llamada Evaluator.
class Evaluator:
    
    # Creamos una función estática, lo que significa que esta función pertenece a la clase Evaluator
    # y no a cualquier objeto de esta clase. Esto significa que no necesitas crear un objeto de la 
    # clase para usar esta función, puedes llamarla directamente a través de la clase.
    @staticmethod
    def zip_evaluate(coefs, words):
        
        # Primero, chequeamos si las longitudes de las dos listas son iguales.
        # Si no lo son, la función retorna -1 y se detiene allí.
        if len(coefs) != len(words):
            return -1
        else:
            # Usamos la función zip para combinar las dos listas en una lista de tuplas. Luego, 
            # para cada tupla, calculamos el producto de la longitud de la palabra (len(w)) y su 
            # coeficiente correspondiente (c). Finalmente, sumamos todos estos productos para obtener 
            # el resultado final.
            return sum(c*len(w) for c, w in zip(coefs, words))

    # Creamos otra función estática que hace lo mismo que la anterior pero de una manera diferente.
    @staticmethod
    def enumerate_evaluate(coefs, words):

        # Al igual que antes, si las longitudes de las listas no son iguales, retornamos -1.
        if len(coefs) != len(words):
            return -1
        else:
            # Usamos la función enumerate para obtener el índice y el valor de cada elemento en la 
            # lista de palabras. Luego, usamos el índice para obtener el coeficiente correspondiente 
            # de la lista de coeficientes, y calculamos el producto del coeficiente y la longitud de la 
            # palabra. Finalmente, sumamos todos estos productos.
            return sum(coefs[i]*len(word) for i, word in enumerate(words))

