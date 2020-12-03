# Eric Leibensperger
# Advent of Code Day 02
# December 2, 2020
########################
import numpy as np
# Goal: Count trees!
# Read in file
dataFile='/Users/eleib003/AOC.2020/03/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]
nRows = np.size(luckey)
nCols = np.size(list(luckey[1]))


#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.
right=[1,3,5,7,1]
down=[1,1,1,1,2]
numTrees=np.zeros(len(right))
product=1

for r in np.arange(0,len(right)):
    rr=right[r]
    dd=down[r]
    currX=0
    currY=0#Rows-1
    while currY <= (nRows-1):
        here = list(luckey[currY])[currX]
        if here=='#':
            numTrees[r]=numTrees[r]+1
        currX=currX+rr
        if(currX > nCols-1):
            currX = currX-nCols
        currY=currY+dd
    product=product*numTrees[r]

print('Number of Trees:',numTrees)
print('Their product:',product)
