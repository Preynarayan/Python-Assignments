import sys
#Program by Prayanshu Narayan S#101144277
def main():
    #Get Variables
    H = sys.argv[1].upper() == "TRUE"
    print("What is the value of B")
    B = input().upper() == "TRUE"
    print("What is the value of F")
    F = input().upper() == "TRUE"
    
    
    #Make sure input is correct
    print(f"B is: {B} and F is {F} H is: {H}")
    
    #All the different Operations
    O1 = not B
    print(f"Not B is: {O1}")
    O2 = O1 and H
    print(f"Not B and H is : {O2}")
    O3 = O2 and F
    print(f"(Not B and H) and F is: {O3} ")
    O4 = not H
    print(f"Not H is : {O4}")
    O5 = O4 or O3
    print(f"((Not B and H) and F)) or (Not H) is: {O5}")
    O6 = not H
    print(f"Not H is : {O6}")
    O7 = O6 or O5
    print(f"(((Not B and H) and F)) or (Not H)) or (Not H) is: {O7}")
    O8 = B or O7
    print(f"((((Not B and H) and F)) or (Not H)) or (Not H)) or B is: {O8}")
    
    
    
    
    
    




main()