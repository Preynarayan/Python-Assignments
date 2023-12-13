#Assignment 5 by Prayanshu Narayan S# 101144277
from comp1405_f23_special_library_loomwork_simplified import *



def main():
    

    wide  = 216
    high = 16
    yesPink = True
    open_window(wide,high)
    for _ in range(12):
        blueStart = 1
        for j in range(18):

            if(j <=5):
                
                if(yesPink == True):
                    for _ in range(high):
                        add_bead("pink")
                    next_thread()
                    yesPink = False
                    
                else:
                    for _ in range(high):
                        add_bead("ember")
                    next_thread()
                    yesPink = True
            if(j>=6 and j<=11):
                
                for k in range(high):
                    if(k == blueStart ):
                        add_bead("dusk")
                        continue
                        
                    add_bead("coral")
                next_thread()
                blueStart += 2
                    
            if(j >= 12):
                for m in range(high):
                    if (m == 3 or m == 11):
                        add_bead("lime")
                        continue
                    add_bead("leather")
                next_thread()
    keep_window()            

main()                    
                
                
            
            


        
    

