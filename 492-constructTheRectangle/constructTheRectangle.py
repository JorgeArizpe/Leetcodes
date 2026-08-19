from math import sqrt

def constructRectangle(area):
    w = int(sqrt(area))
    while area%w != 0:
        w -= 1
    return[int(area/w), w]

area = 122122

print(constructRectangle(area))
