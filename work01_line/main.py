from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0,0,500,100,screen,color)
draw_line(0,0,100,500,screen,color)
draw_line(0,500,100,0,screen,color)
draw_line(0,500,500,400,screen,color)
draw_line(100,100,500,100,screen,color)
draw_line(100,100,100,500,screen,color)
draw_line(0,0,500,500,screen,color)
draw_line(0,500,500,0,screen,color)

for x in range(20):
    for y in range(50):
        draw_line(x,y,y,x,screen,color)

for x in range(300):
    draw_line(150,100,x,x,screen,color)


display(screen)
save_extension(screen, 'img.png')
