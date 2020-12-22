# Eric Leibensperger
# Advent of Code Day 08
# December 20, 2020
########################
import numpy as np
# Goal: break that infinite loop
# Read in file
dataFile='/Users/eleib003/AOC.2020/08/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]
    
nRows = np.size(luckey)
data=[]
for n in np.arange(0,nRows):
    splitUp=luckey[n].split()
    data.append([splitUp[0],int(splitUp[1]),False])
    
keepGoing=True
acc=0
n=0
while keepGoing:
    instruction=data[n][0]
    val=data[n][1]
    step=1
    if(instruction=='acc'):
        acc+=val
        step=1
        data[n][2]=True
    if(instruction=='jmp'):
        step=val
        data[n][2]=True
        
    n+=step
    if(data[n][2]):
        keepGoing=False

print('Accumulator: ',acc)