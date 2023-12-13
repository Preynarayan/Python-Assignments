#Assignment 4 by Prayanshu Narayan S#101144277

#main function
def main():
    #ask the user the diagnostic questions about the flower (converting responses to uppercase letters)
    petalColour = input("What is the colour of the petals (Orange or Ember): ").upper()
    petalShape = input("What is the shape of the petals (Round or Not Round): ").upper()
    petalNumber = input("What is the number of the petals (4 or 6): ").upper()
    centreShape = input("What is the shape of the centre (Circle or Star): ").upper()
    centreColour = input("What is the colour of the centre (Black or Sky): ").upper()
    sepalColour = input("What is the colour of the sepals (Moss or Tea): ").upper()
    
    #this is the nested structure that allows the program to identify the flower
    
    if(petalColour == "ORANGE"):
        print("Your flower is C")
    else:
        if(centreShape == "STAR"):
            print("Your flower is D")
        else:
            if(centreColour == "SKY"):
                print("Your flower is A")
            else:
                if(sepalColour == "TEA"):
                    print("Your flower is B")
                else: 
                    if(petalNumber == "6"):
                        print("Your flower is F")
                    else: 
                        if(petalShape == "ROUND"):
                            print("Your flower is E")
                        else:
                            print("Your flower is G")
    
    
#call the main function
main()