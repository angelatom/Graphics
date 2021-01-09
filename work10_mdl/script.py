import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    print symbols

    for command in commands:
        curr = command['op']
        args = command['args']
        if curr == 'push':
            stack.append([x[:] for x in stack[-1]])
        elif curr == 'pop':
            stack.pop()
        elif curr == 'scale':
            t = make_scale(float(args[0]),
                           float(args[1]),
                           float(args[2]))
            matrix_mult(stack[-1], t)
            stack[-1] = [x[:] for x in t]
        elif curr == 'move':
            t = make_translate(float(args[0]),
                               float(args[1]),
                               float(args[2]))
            matrix_mult(stack[-1], t)
            stack[-1] = [x[:] for x in t]
        elif curr == 'rotate':
            theta = float(args[1]) * (math.pi / 180)
            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(stack[-1], t)
            stack[-1] = [x[:] for x in t]
        elif curr == 'display':
            display(screen)
        elif curr == 'save':
            save_extension(screen, args[0] + '.png')
            screen = new_screen()
            zbuffer = new_zbuffer()
        elif curr == 'line':
            add_edge(tmp, float(args[0]), float(args[1]),
                     float(args[2]), float(args[3]),
                     float(args[4]), float(args[5]))
            matrix_mult(stack[-1], tmp)
            draw_lines(tmp, screen, zbuffer, color)
            tmp = []
        elif curr == 'circle':
            add_circle(tmp, float(args[0]), float(args[1]),
                       float(args[2]), float(args[3]), step_3d)
            matrix_mult(stack[-1], tmp)
            draw_lines(tmp, screen, zbuffer, color)
            tmp = []
        elif curr == 'sphere':
            add_sphere(tmp, float(args[0]), float(args[1]),
                       float(args[2]), float(args[3]), step_3d)
            matrix_mult(stack[-1], tmp)
            if (command['constants']):
                c = command['constants']
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, c)
            tmp = []
        elif curr == 'torus':
            add_torus(tmp, float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step_3d)
            matrix_mult(stack[-1], tmp)
            if (command['constants']):
                c = command['constants']
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, c)
            tmp = []
        elif curr == 'box':
            add_box(tmp, float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]))
            matrix_mult(stack[-1], tmp)
            if (command['constants']):
                c = command['constants']
            draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, c)
            tmp = []