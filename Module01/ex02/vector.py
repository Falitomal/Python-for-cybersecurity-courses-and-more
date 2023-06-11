# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 17:46:37 by jledesma          #+#    #+#              #
#    Updated: 2023/04/16 17:46:38 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
    def __init__(self, values):
        if isinstance(values, list):
            if all(isinstance(x, list) for x in values):
                self.values = values
                self.shape = (len(values), len(values[0]) if values else 0)
            else:
                self.values = [[x] for x in values]
                self.shape = (len(values), 1)
        else:
            raise ValueError("Invalid values")

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)

    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must be of the same shape")
        if len(self.shape) == 1:
            return sum(a[0]*b[0] for a, b in zip(self.values, other.values))
        else:
            return sum(a[0]*b[0] for a, b in zip(self.values[0], other.values[0]))

    def T(self):
        if len(self.shape) == 1:
            return Vector([self.values])
        else:
            return Vector([[x] for x in self.values[0]])

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shapes of vectors do not match.")
        if len(self.shape) == 1:
            return Vector([a[0]+b[0] for a, b in zip(self.values, other.values)])
        else:
            return Vector([[a+b for a, b in zip(self.values[0], other.values[0])]])

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shapes of vectors do not match.")
        if len(self.shape) == 1:
            return Vector([a[0]-b[0] for a, b in zip(self.values, other.values)])
        else:
            return Vector([[a-b for a, b in zip(self.values[0], other.values[0])]])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Vector([a[0]*other for a in self.values])
            else:
                return Vector([[a*other for a in self.values[0]]])
        else:
            raise TypeError("Invalid type for multiplication.")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            if len(self.shape) == 1:
                return Vector([a[0]/other for a in self.values])
            else:
                return Vector([[a/other for a in self.values[0]]])
        else:
            raise TypeError("Invalid type for division.")


    def __rtruediv__(self, other):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
