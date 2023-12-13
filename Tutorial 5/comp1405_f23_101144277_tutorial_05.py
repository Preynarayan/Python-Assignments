#Tutorial 5 by Prayanshu Narayan S#101144277



#Function: isPrime
#Description: checks if a number is prime or not
#param: number
#return: boolean
def isPrime(number: int) -> bool:
    i = 2
    if number == 1:
        return True
    while i  != number:
        if number % i == 0:
            return False
        i += 1
    return True

#main function
def main():
    flag = True
    while(flag):
        try:
            number = int(input("Enter a number: (-1 to quit)"))
            if number ==-1:
                break


            if isPrime(number):
                print("The number is prime")
            else:
                print("The number is not prime")
            
            
        except ValueError:
            print("Please enter a valid number")
            flag = True
    
main()