def main():
    
    open_window(750,750)
    
    for i in range(15):
        if(i == 1):
            for j in range(15):
                if(j == 2 or j ==4 or j == 6 or j == 8):
                    umbrella(i,j,"GREEN")
        if(i == 4):
            for j in range(15):
                if(j == 2 or j ==4 or j == 6 or j == 8):
                    umbrella(i,j,"GREEN")
                if(j == 3 or j ==7 or j == 1):
                    triangle(i,j,"BLUE")
        if(i == 7):
            for j in range(15):
                if(j == 2 or j ==4 or j == 6 or j == 8):
                    umbrella(i,j,"GREEN")
        
        if(i == 8):
            for j in range(15):
                if(j == 3 or j ==7 or j == 1):
                    triangle(i,j,"BLUE")
        
            
    
    keep_window()
    
main()