# Eric Leibensperger
# Advent of Code Day 09
# December 21, 2020
########################
import numpy as np
from itertools import combinations
# Goal: break the cypher
# Read in file
dataFile='/Users/eleib003/AOC.2020/09/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [int(line.rstrip()) for line in f]

    
nRows = np.size(luckey)
preamble=25

def combos(dataIn):
    combs=combinations(dataIn,2)
    sums=[]
    for i in list(combs):
        sums.append(sum(i))
    
    return sums

go=True
r=preamble
while go:
    combs=combos(luckey[r:(r+preamble)])
    number=luckey[r+preamble]
    if number in combs:
        print(number,combs.index(number))
        r+=1
    else:
        go=False

print('First number not in sums of previous 25: ',number)

# Where can we find two numbers that sum to our erroneous number?
go=True
beg=26
end=beg+2
while go:
    print(beg,end)
    sumUp=sum(luckey[beg:end])
    if(sumUp==number):
        go=False
    elif(sumUp>number):
        beg+=1
        end=beg+2
    else:
        end+=1


print('Sum of smallest and largest numbers:',min(luckey[beg:end])+max(luckey[beg:end]))
