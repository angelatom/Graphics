from random import randint

pic = open("image.ppm", "w")

def createpic():
    header = "P3 500 500 255 "
    pic.write(header)
    for x in range(500):
        for y in range(500):
            z = randint(0,255)
            color0 = x * y * z % 256 
            color1 = (x + y) % 256
            color2 = randint(0,255)
            pic.write(str(color0) + " " + str(color1) + " " + str(color2) + " ")

createpic()