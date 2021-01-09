from display import *


def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 > x0):
        x = x0
        y = y0 
    else:
        x = x1
        y = y1
        x1 = x0
        y1 = y0
    A = y1 - y0
    B = -1 * (x1 - x0)  
    dy = y1 - y0
    dx = x1 - x0  
    if (dx != 00):
        m = dy / dx 
    if (x1 == x0):
        d = 2 * B + A
        while y <= y1:
            plot(screen, color, x, y)
            if (d < 0):
                x += 1 
                d += 2 * A
            y += 1
            d += 2 * B
    elif (m >= 0 and m < 1):
        d = 2 * A + B 
        while x <= x1:
            plot(screen, color, x, y)
            if (d > 0):
                y += 1 
                d += 2 * B
            x += 1
            d += 2 * A
    elif (m >= 1):
        d = 2 * B + A
        while y <= y1:
            plot(screen, color, x, y)
            if (d < 0):
                x += 1 
                d += 2 * A
            y += 1
            d += 2 * B
    elif (m < 0 and m >= -1):
        d = 2 * A - B
        while x <= x1:
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1 
                d -= 2 * B
            x += 1
            d += 2 * A
    else:
        d = 2 * B - A
        while y >= y1:
            plot(screen, color, x, y)
            if (d < 0):
                x += 1 
                d += 2 * A
            y -= 1
            d += 2 * B
