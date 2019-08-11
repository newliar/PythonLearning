import math

def quadratic(a, b, c):
    x_1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    x_2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    return x_1, x_2