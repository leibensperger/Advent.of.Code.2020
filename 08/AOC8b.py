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

nn=0
notFound=True
while notFound:
    print('nn:',nn)
    keepGoing=False
    update=False
    if(data[nn][0] == 'jmp'):
        old='jmp'
        data[nn][0]='nop'
        keepGoing=True
        update=True
    elif(data[nn][0] == 'nop'):
        old='nop'
        data[nn][0]='jmp'
        keepGoing=True
        update=True
        
    acc=0
    n=0
    while keepGoing:
        instruction=data[n][0]
        val=data[n][1]
        step=1
        if(instruction=='acc'):
            acc+=val
            data[n][2]=True
        if(instruction=='jmp'):
            step=val
            data[n][2]=True
        
        n+=step
        if(data[n][2] or n == (nRows-1)):
            keepGoing=False
            
    if(n == (nRows-1)):
        notFound=False
    else:
        if update: 
            data[nn][0]=old
        for nnn in np.arange(0,nRows):
            data[nnn][2]=False
        nn+=1


print('Accumulator: ',acc)