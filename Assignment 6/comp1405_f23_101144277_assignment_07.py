#Assignment 6 by Prayanshu Narayan S#101144277
from random import *

import sys


#Question 1: What was the base case of the argument for the recursive implementation of the third function?
#Awswer: The base case of the argument for the recursive implementation of the third function was an empty list.

#Question 2: How did you simplify an arugment that was not the base case so that it is closer to the base case?



#Function to create a list of random numbers
#param: none
#return: list of random numbers
def CreateList()-> list:
    list1 = []
    
    while True:
        rand = randint(1, 10)
        list1.append(rand)
        print(f"List is {list1}")
        if(input("Do you want to continue?").upper() == "NO"):
            break
        
    return list1

#function to find a value in a list and remove it 3 times
#param: list of random numbers
#return: list of random numbers
def FindValue(list1: list) ->list:
    
    
    for _ in range(3):
        value = int(input("Enter a value to find: "))
        range1 = len(list1)
        for i in range(range1):
            if(list1[i] == value):
                list1.pop(i)
                break
#placeholder function
#param: list of random numbers
#return: list of random numbers
def placeholder(list1: list) -> list:
    resultList = []
    i = 0
    length = len(list1)
    while i < length:
       
        if(list1[i] != 2):
            resultList.append(list1[i])


        i = i+1
    return resultList    
# recreate placeholder function using recursion
#param: list of random numbers
#return: list of random numbers

def plchlderRecursive(list1: list):
    i = 0
    if list1 == []:
        return []
    
    if i > len(list1):
        return list1
    if list1[0] != 2:
        i = i+1
        return [list1[0]] + plchlderRecursive(list1[1:])
    else:
        return plchlderRecursive(list1[1:])
    
    
    
        
 

    
#main function
#param: none
#return: none
def main():
    
    
    
    
    

    
    
    mainList = []
    mainList = CreateList()
    FindValue(mainList)
  
    #command line arguement
    if(len(sys.argv) == 1):
        print("No command line arguement")
        print("Please restart program and enter a command line arguement, either recursive or nonrecursive")        
    if(len(sys.argv) == 2):
        if(sys.argv[1].upper() == "RECURSIVE"):
            print(plchlderRecursive(mainList))
        elif(sys.argv[1].upper() == "NONRECURSIVE"):
            print(placeholder(mainList))
        else: 
            print("Invalid command line arguement")
            

    
    
        
main()
        
    