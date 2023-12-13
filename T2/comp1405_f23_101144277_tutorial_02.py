

print("Enter your average tutorial grade: \n")
tutorial = float(input())
print("Enter your average quiz grade: \n")
quiz = float(input())
print("Enter your average assignment grade: \n")
assignment = float(input())
print("Enter your final exam grade: \n")
exam = float(input())

numGrade = (0.1*tutorial) + (0.3*quiz) + (0.4*assignment) + (0.2*exam)

if(numGrade >=90 and numGrade <= 100 ):
    letterGrade = "A+"
elif(numGrade >=85 and numGrade < 90 ):
    letterGrade = "A"
elif(numGrade >=80 and numGrade < 85 ):
    letterGrade = "A-"
elif(numGrade >=77 and numGrade < 80 ):
    letterGrade = "B+"
elif(numGrade >=73 and numGrade < 77 ):
    letterGrade = "B"
elif(numGrade >=70 and numGrade < 73 ):
    letterGrade = "B-"
elif(numGrade >=67 and numGrade < 70 ):
    letterGrade = "C+"
elif(numGrade >=63 and numGrade < 67 ):
    letterGrade = "C"
elif(numGrade >=60 and numGrade < 63 ):
    letterGrade = "C"
elif(numGrade >=57 and numGrade < 60 ):
    letterGrade = "D+"
elif(numGrade >=53 and numGrade < 57 ):
    letterGrade = "D"
elif(numGrade >=50 and numGrade < 53 ):
    letterGrade = "D-"
elif(numGrade >=0 and numGrade < 50 ):
    letterGrade = "F"
    
    
print(f"Your letter Grade is {letterGrade}.")

