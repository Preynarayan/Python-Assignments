import sys



def add_rooms_from_file(filename: str):
    #open file
    file = open(filename, "r")
    
    for line in file:
        split_line = line.split('",',1)
        room = split_line[0].split('"')[1]
        items = split_line[1].strip(' [] ",\n').split('", "')
        

        



add_rooms_from_file("TEST.txt")