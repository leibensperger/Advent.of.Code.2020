# Eric Leibensperger
# Advent of Code Day 06
# December 6, 2020
########################
import numpy as np
# Goal: Find your seat!
# Read in file
dataFile='/Users/eleib003/AOC.2020/06/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]
nRows = np.size(luckey)

# Loop through all and find the number of unique people answering yes
IDs=[]
sumUpa=0
sumUpb=0
first=True
for n in luckey:
    print(n)
    if(n==''):
        print(n,len(IDs),IDs)
        sumUpa = sumUpa + len(IDs)
        IDs=[]
        
        sumUpb= sumUpb + len(potentials)
        first=True
    else:
        if(first):
            potentials=n
            first=False
        for nn in np.arange(0,len(n)):
            if(n[nn] not in IDs): 
                IDs.append(n[nn])
        newPotentials=[]
        for p in potentials:
            if(p in n): 
                newPotentials.append(p)
        potentials=newPotentials.copy()
    

print(n,len(IDs),IDs)
sumUpa = sumUpa + len(IDs)
sumUpb= sumUpb + len(potentials)

print('Sum for part A: ',sumUpa)
print('Sum for part B:', sumUpb)
