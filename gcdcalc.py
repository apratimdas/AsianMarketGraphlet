
from graphics import *
from random import randint
import csv
import sys
import math
import colorsys

grid = []
for i in range(11):
    grid.append([])
    for j in range(11):
        grid[i].append(j)

# print(grid)

gcm1=[]
gcm2=[]

with open(sys.argv[1]) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        gcm1.append(row)

with open(sys.argv[2]) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        gcm2.append(row)



print(gcm1)
print(gcm2)

sumctr = 0
gcm1ctr = 0

for i in range(0,15):
    for j in range(i,15):
        sumctr += (float(gcm1[i][j]) - float(gcm2[i][j]))**2
        gcm1ctr += float(gcm1[i][j])

print(math.sqrt(sumctr))
print(math.sqrt(sumctr)/gcm1ctr)
print(1 - math.sqrt(sumctr)/gcm1ctr)


def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value-minimum) / (maximum - minimum)
    b = int(max(0, 255*(1 - ratio)))
    r = int(max(0, 255*(ratio - 1)))
    g = 255 - b - r
    return [r, g, b]

def main():
    win = GraphWin("My Window", 600, 600)
    squares = []
    i=0
    j=0
    while i < 15:
        j=0
        while j < 15:
            square = Rectangle(Point(j*40,i*40), Point((j+1)*40,(i+1)*40))
            x = gcm[i][j]
            y = -float(x) + 1.0
            rval = int(y / 2 * 255)
            bval = int( (1 - y / 2) * 255)
            # rval = int(y / 2 * 255)
            rgb = colorsys.hsv_to_rgb(((y/2)*255)/360.0, 1.0, 0.7)
            rgbn = [int(x*255) for x in rgb]
            square.setFill(color_rgb(rgbn[0],rgbn[1],rgbn[2]))
            squares.append(square)
            square.draw(win)
            j+=1
        i+=1

    win.getMouse()


# main()