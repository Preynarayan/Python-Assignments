#Assignment 6 by Prayanshu Narayan S#101144277
from random import *
from typing import List


#Function to create a list of random numbers
#param: none
#return: list of random numbers
def CreateList()-> List[int]:
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
def FindValue(list1: List[int]) -> List[int]:
    
    
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
def placeholder(list1: List[int]) -> List[int]:
    resultList = []
    i = 0
    while i < len(list1):
        if(list1[i] != 2):
            
            resultList.append(list1.pop(i))
        i = i+1
    return list1      

    
#main function
#param: none
#return: none
def main():
    mainList = []
    mainList = CreateList()
    FindValue(mainList)
    print(mainList)
    print(placeholder(mainList))
    
main()
        
    