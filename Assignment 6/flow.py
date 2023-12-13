def FindValue(list1: List[int]) -> List[int]:
    value = int(input("Enter a value to find: "))
    
    for _ in range(3):
        range1 = len(list1)
        for i in range(range1):
            if(list1[i] == value):
                list1.pop(i)
                break