import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    a = calculate_ambient(ambient,areflect)
    d = calculate_diffuse(light,dreflect,normal)
    s = calculate_specular(light,sreflect,view,normal)
    return [ limit_color(int(a[0] + d[0] + s[0])),
             limit_color(int(a[1] + d[1] + s[1])),
             limit_color(int(a[2] + d[2] + s[2])),
           ]

def calculate_ambient(alight, areflect):
    return [ limit_color(alight[0] * areflect[0]),
             limit_color(alight[1] * areflect[1]),
             limit_color(alight[2] * areflect[2]),
           ]

def calculate_diffuse(light, dreflect, normal):
    l = light[LOCATION]
    normalize(l)
    normalize(normal)
    return [ limit_color(light[1][0] * dreflect[0] * dot_product(normal,l)),
             limit_color(light[1][1] * dreflect[1] * dot_product(normal,l)),
             limit_color(light[1][2] * dreflect[2] * dot_product(normal,l)),
           ]

def calculate_specular(light, sreflect, view, normal):
    l = light[LOCATION]
    normalize(l)
    normalize(normal)
    normalize(view)
    dot = 2 * dot_product(light[0],normal)
    dot_product_me = [ normal[0] * dot - light[0][0],
                       normal[1] * dot - light[0][1],
                       normal[2] * dot - light[0][2],
                     ]
    r = dot_product(dot_product_me,view)
    if r < 0:
      r = 0
    r = math.pow(r,4)
    return [ limit_color(light[1][0] * sreflect[0] * r),
             limit_color(light[1][1] * sreflect[1] * r),
             limit_color(light[1][2] * sreflect[2] * r),
           ]

def limit_color(color):
    if color < 0:
      return 0
    elif color > 255:
      return 255
    else:
      return color

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
