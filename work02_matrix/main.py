from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
m2 = []



print ("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
add_edge(m2,1,2,3,4,5,6)
print_matrix(m2)



print ("Testing ident. m1 =")
m1 = new_matrix()
m1 = ident(m1)
print_matrix(m1)



print ("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)



print ("Testing Matrix mult. m1 =")
m1 = [ ]
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,10,11,12)
print_matrix(m1)



print ("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1,m2)
print_matrix(m2)


matrix = []
add_edge(matrix,400,400,0,0,400,0)
add_edge(matrix,0,400,0,350,100,0)
add_edge(matrix,350,100,0,200,500,0)
add_edge(matrix,200,500,0,50,100,0)
add_edge(matrix,50,100,0,400,400,0)

draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'pic.png')
