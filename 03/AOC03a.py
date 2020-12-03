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
currX=0
currY=0#Rows-1
numTrees=0
while currY <= (nRows-1):
    here = list(luckey[currY])[currX]
    if here=='#':
        numTrees=numTrees+1
    currX=currX+3
    if(currX > nCols-1):
        currX = currX-nCols
        print('Looping!')
    currY=currY+1
    #currY=currY-1
    
