import math
num = 0
def phoneNumber(phoneNum):
    num = int(phoneNum)
    prefix  = num // 10000
    line  = num %10000
    
    result = 0
    
    


    result = prefix*500
    print("your prefix is ", num, ". Multiply this by 500 and the result is: ", result, "\n")
    result = (result + 10 ) * 60
    print("Add 10 to that result and multiply it by 60, and the result is: ", result, "\n")
    result = result + (3*line)
    print("Your line number is ", line,  ". Add this to the previous result three times, and the result is:", result, "\n")
    result = (result -600)/3
    print("Subtract 600 from that result and divide it by 3, and the result is:", int(result))
    

    



num = input("Enter your sever-digit phone number: ")
phoneNumber(num)


