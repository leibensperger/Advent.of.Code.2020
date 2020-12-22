# Eric Leibensperger
# Advent of Code Day 07
# December 7, 2020
########################
import numpy as np
# Goal: Bags galore
# Read in file
dataFile='/Users/eleib003/AOC.2020/07/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]
nRows = np.size(luckey)

#Loop through, adding to dictionary
bagDict=dict()
contains=list()
for line in np.arange(0,nRows):
    splitUp=luckey[line].split('contain')
    outer=splitUp[0][0:(len(splitUp[0])-6)]
    contents=list()
    inners=splitUp[1].split(',')
    nInners=len(inners)
    
    for n in np.arange(0,nInners):
        thisOne=inners[n].split('bag')[0]
        num=thisOne[1]
        color=thisOne[3:(len(thisOne)-1)]
        contents.append(color)
        if(color=='shiny gold'):
            contains.append(outer)
    
    bagDict[outer]=contents
    
number=len(contains)

n=0
while( n < len(contains)):
    print(n,len(contains))
    for out,inn in bagDict.items():  
        for nn in np.arange(0,len(inn)):
            if (inn[nn] == contains[n]) and (out not in contains):
                contains.append(out)
    n+=1

print(len(contains))
    

