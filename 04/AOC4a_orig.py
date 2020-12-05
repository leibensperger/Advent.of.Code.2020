# Eric Leibensperger
# Advent of Code Day 04
# December 4, 2020
########################
import numpy as np
# Goal: Find valid passports or N.P. credentials
# Read in file
dataFile='/Users/eleib003/AOC.2020/04/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]
    
nRows = np.size(luckey)

fields=[]
haveCID=False
count=0
for r in np.arange(0,nRows):
    thisOne=list(luckey[r])
    if(thisOne==[]):
        print('New one!')
        if len(fields)==8 or (len(fields)==7 and not(haveCID)):
            count=count+1
            print(len(fields),fields)
        fields=[]
        haveCID=False
    else:
        here=[i for i, e in enumerate(thisOne) if e == ':']
        nFound=len(here)
        for h in here:
            toAdd=thisOne[h-3]+thisOne[h-2]+thisOne[h-1]
            fields.append(toAdd)
            if(toAdd == 'cid'):
                haveCID=True
                
print('Number of Valids:',count)
