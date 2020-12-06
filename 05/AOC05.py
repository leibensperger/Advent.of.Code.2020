# Eric Leibensperger
# Advent of Code Day 05
# December 5, 2020
########################
import numpy as np
# Goal: Find your seat!
# Read in file
dataFile='/Users/eleib003/AOC.2020/05/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]
nRows = np.size(luckey)

# Loop through all and update max value 
# Also store all IDs
IDs=[]
maxVal=0
for n in luckey:
    rBin=n[0:7]
    rBin=rBin.replace('B','1')
    rBin=rBin.replace('F','0')
    row=int(rBin,2)
    
    cBin=n[7:10]
    cBin=cBin.replace('R','1')
    cBin=cBin.replace('L','0')
    col=int(cBin,2)
    
    valHere=row*8 + col
    IDs.append(valHere)
    if(valHere > maxVal): maxVal=valHere

print('Highest seat ID: ',maxVal)

# If summed up IDs, difference from the sum of all possible IDs from lowest
# to highest is the one missing:
myRow=sum(np.arange(min(IDs),max(IDs)+1))-sum(IDs)
print('My row is: ',myRow)