#Turotial 4 by Prayanshu Narayan 101144277
import random

def generate_random_number():
    return random.randint(1,10)

#main function

def main():
    num = 0
    strng = ""
    random_numbers = []
    sizeArr = int(input("How long would you like the intial list to be? "))
    for i in range(sizeArr):
        random_numbers.append(generate_random_number())
    print(f"The list is currently: {random_numbers}")
    while(num != -1):
        
        num = int(input("What number would you like to replace (or -1 to exit))? "))
        if(num == -1):
            break
        strng = input("What string would you like to use as replacement? ")
        for i in range(len(random_numbers)):
            if(random_numbers[i] == num):
                random_numbers[i] = strng
        print(f"The list is currently: {random_numbers}")
    
        
main()