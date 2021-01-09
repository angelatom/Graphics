from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
      txt = open(fname, "r")
      lines = txt.readlines()
      the_list = []
      for x in lines:
            the_list.append(x.strip())
      print(the_list)
      counter = 0
      while counter < len(the_list):
            line = the_list[counter]
            print(line)
            if line == "line":
                  args = the_list[counter+1].split(" ")
                  add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
                  counter += 2
            elif line == "ident":
                  ident(transform)
                  counter += 1
            elif line == "scale":
                  args = the_list[counter+1].split(" ")
                  matrix_mult(make_scale(int(args[0]), int(args[1]), int(args[2])), transform)
                  counter += 2
            elif line == "translate":
                  args = the_list[counter+1].split(" ")
                  matrix_mult(make_translate(int(args[0]),int( args[1]), int(args[2])), transform)
                  counter += 2
            elif line == "rotate":
                  args = the_list[counter+1].split(" ")
                  if args[0] == "x":
                        rotation = make_rotX(int(args[1]))
                  elif args[0] == "y":
                        rotation = make_rotY(int(args[1]))
                  else:
                        rotation = make_rotZ(int(args[1]))
                  matrix_mult(rotation, transform)
                  counter += 2
            elif line == "apply":
                  matrix_mult(transform, points)
                  counter += 1
            elif line == "display":
                  clear_screen(screen)
                  print(points)
                  draw_lines(points, screen, color)
                  print(points)
                  display(screen)
                  counter += 1
            elif line == "save":
                  clear_screen(screen)
                  draw_lines(points, screen, color)
                  arg = the_list[counter+1]
                  save_extension(screen, arg)
                  counter += 2
            elif line == "quit":
                  counter = len(the_list)
            else:
                counter += 1

                  

