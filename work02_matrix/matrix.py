"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    result = ""
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result = result + str(matrix[j][i]) + "  "
        result += "\n"
    print(result)     

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    m = []
    side = len(matrix)
    for x in range(side):
        m.append( [] )
        for y in range(side):
            if (x == y):
                m[x].append( 1 )
            else:
                m[x].append( 0 )
    return m


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix(4,len(m2))
    for i in range(4): 
        for col in range(len(m2)):
            prod = 0
            for n in range(len(m1)):
                prod += (m1[n][i] * m2[col][n])
            temp[col][i] = prod
    for i in range (4):
        for j in range(len(m2)):
            m2[j][i] = temp[j][i]
    return m2


def new_matrix(rows=4,cols=4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows):
            m[c].append( 0 )
    return m
