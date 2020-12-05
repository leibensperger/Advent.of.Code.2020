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
valid=True
countA=0
countB=0
eyeColors=['amb','blu','brn','gry','grn','hzl','oth']
for r in np.arange(0,nRows):
    thisOne=luckey[r].split()
    nRec=len(thisOne)
    if(thisOne==[]):
        #print('New one!')
        if (len(fields)==8 or (len(fields)==7 and not(haveCID))):
            countA+=1
        if valid and (len(fields)==8 or (len(fields)==7 and not(haveCID))):
            countB+=1
        fields=[]
        haveCID=False
        valid=True
    else:
        for rec in thisOne:
            field=rec.split(':')[0]
            data=rec.split(':')[1]
            fields.append(field)
            #byr (Birth Year) - four digits; at least 1920 and at most 2002.
            #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            #hgt (Height) - a number followed by either cm or in:
                #If cm, the number must be at least 150 and at most 193.
                #If in, the number must be at least 59 and at most 76.
            #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            #pid (Passport ID) - a nine-digit number, including leading zeroes.
            #cid (Country ID) - ignored, missing or not.
            if(field == 'cid'): haveCID=True
            elif(field == 'byr'): 
                if(len(data)!=4 or int(data)<1920 or int(data)>2002):  valid=False
            elif(field == 'iyr'): 
                if(len(data)!=4 or int(data)<2010 or int(data)>2020):  valid=False
            elif(field == 'eyr'): 
                if(len(data)!=4 or int(data)<2020 or int(data)>2030):  valid=False
            elif(field == 'hcl'): 
                if(len(data)!=7 or data[0]!='#'):  valid=False
            elif(field == 'ecl'): 
                if(not(data in eyeColors)):  valid=False
            elif(field == 'pid'): 
                if(len(data)!=9):  valid=False
            elif(field == 'hgt'):
                lenHgt=len(data)
                unit=data[(lenHgt-2):lenHgt]
                if(unit == 'in' or unit =='cm'):
                    if(unit=='in'):
                        minVal=59
                        maxVal=76
                    else: 
                        minVal=150
                        maxVal=193
                    height=int(data[0:(lenHgt-2)])
                    if(height < minVal or height > maxVal):  valid=False
                else: valid=False
                


    

                
print('Number of Valids in Part A:',countA)
print('Number of Valids in Part B:',countB)
