# Eric Leibensperger
# Advent of Code Day 01
# December 1, 2020
########################

# Goal: Read in a list of files and find the two that sum to 2020. Next
# find the product of those numbers.
import numpy as np
# Read in file
dataFile='/Users/eleib003/AOC.2020/01/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    lines = [line.rstrip() for line in f]
# Convert the values to integers rather than strings
vals=np.array(lines,dtype='int')

# Find the number of values
nVals=len(vals)

# This is brute force. Loop through the values and find the ones that add up to 
# 2020
for n1 in np.arange(0,nVals):
    # Only need took at n1+1 to the end since others already inspected
    for n2 in np.arange(n1+1,nVals):
        # If this is what we want, break out of the inner loop
        if(vals[n1]+vals[n2] == 2020): 
            break 
    # Again, if this is what we want, break out of the outer loop
    if(vals[n1]+vals[n2] == 2020): 
        break 
        
# Print the results!
print('Values summing to 2020 and their product: ',vals[n1],vals[n2],vals[n1]*vals[n2])
done=False
for n1 in np.arange(0,nVals):
    for n2 in np.arange(n1+1,nVals):
        for n3 in np.arange(n2+1,nVals):
            if(vals[n1]+vals[n2]+vals[n3] == 2020): 
                done=True
                break
        if(done): 
                break
    if(done): 
                break
# Print the results!
print('Values summing to 2020 and their product: ',vals[n1],vals[n2],vals[n3],vals[n1]*vals[n2]*vals[n3])