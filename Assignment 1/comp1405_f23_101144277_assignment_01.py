#Assignment 1 for COMP 1405 Prayanshu Narayan S#:101144277
#When creating i am viewing my work. the circle is not centred even though my coordinates are right and the insert grid option is 
# not the same grid as the one shown in the assignment docuement. I spoke with TA Ephram and he couldnt fix the problem. 

from comp1405_f23_special_library_easy_graphics_for_101144277 import *
open_window(840,840) #open window to size 840 x 840

fill_window("white") #fill window with a white background colour





draw_circ("sea",420,420,420) #draw a circle with centre (420,420) and radius 420

#List of Coordinates for wine coloured polygon
lx1 = [252,168,168,252,336,252]
ly1 = [105,210,420,525,420,420]

#List of Coordinates for midnight coloured polygon
lx2 = [252,252,336,336]
ly2 = [210,420,420,315]

#draw both polygons
draw_poly(lx1,ly1,"wine")
draw_poly(lx2,ly2,"midnight")


#use this to see the creation
#keep_window()







