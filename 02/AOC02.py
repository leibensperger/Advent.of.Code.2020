# Eric Leibensperger
# Advent of Code Day 02
# December 2, 2020
########################
import numpy as np
# Goal: Read in a list of passwords, required character, and potential position
# in the passworld
# Read in file
dataFile='/Users/eleib003/AOC.2020/02/input.txt'
# Read all of the values and strip off the newline character \n
with open(dataFile) as f:
    luckey = [line.rstrip() for line in f]

# Set up our counts for parts a and b
countA=0
countB=0
# Loop through each of the passwords in the file
for n in np.arange(0,len(luckey)-1):
    # from the first component, extract the low and high locations 
    # that letter could be in password
    low,high=list(map(int,luckey[n].split()[0].split('-') ))
    # extract the necessary letter
    letter = luckey[n].split()[1].split(':')[0]
    # isolate the password itself
    third = list(luckey[n].split()[2])
    # Find thenumber of times the character appears in the password
    num = len([i for i in range(len(third)) if third[i] == letter])
    # If it is greater than our lowest value and lower than our highest, count
    if(num >= low and num <= high):
        countA=countA+1
    # For part b, determin if the letter is at the low or high position but
    # not at both.
    # Here is a logical testing if it is in on or the other
    single=third[low-1] == letter or third[high-1] == letter
    # Here is a logical testing if it is in both locatins
    both=third[low-1] == letter and third[high-1] == letter
    # if it's at one location but not both, tally up
    if(single and not(both)):
        countB=countB+1

print('The number of passwords with the letter between indices: ',countA)
print('The number of passwords with the letter at the low or high index (not both): ',countB)

