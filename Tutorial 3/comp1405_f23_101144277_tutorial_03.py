


def main():
    runNum = int(input())
    if(runNum >= 1 and runNum <=9):
        for x in range(runNum+1):
            for i in range(x):
                print(x, end="")
            print()
    else:
        quit()



        
    


main()