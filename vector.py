# vector is a tensors in numerical computation, we need to descriptions of directions on numbers, so we use this.
# we also know the all mathematical operations on scalars numbers as sum, cross or divide or any basic numbers but in physicst need to giving informations of directions.
# A vector in a simple term can be considered as a single-dimensional array. With respect to Python,
# a vector is a one-dimensional array of lists. It occupies the elements in a similar manner as that of a Python list.
# (https://www.digitalocean.com/community/tutorials/vectors-in-python)

import numpy as np
numpy.array(list)
lst=[10,20,30,40]
vctr=np.array(list)
print("vector created from a list", vctr)

# ADDITION
import numpy as np
list1=[10,20,30,40,50]
list2=[1,2,3,4]
vector1= np.array(list1)
vector2= np.array(list2)
vectors_add=vector1+vector2
vectors_sub=vector1-vector2
vectors_mul=vector1*vector2
vectors_div=vector1/vector2
print("here addition of your vectors",vectors_add)
print("here subtraction of your vectors",vectors_sub)
print("here multiplacation of your vectors",vectors_mul)
print("here division of your vectors",vectors_div)

# DOT PRODUCT
vectors_dot=vector1.dot(vector2)
print("here dot production of your vectors",vectors_dot)

# CROSS PRODUCT
vectors_cro=np.array(vector1,vector2)
print("here cross production of your vectors",vectors_cro)
# define functions to calculate cross product just have 3 elements matrix
def cross_pro(a,b):
    result=\
        [
            a[1]*b[2]-a[2*b[1]],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]
        ]
    return result



