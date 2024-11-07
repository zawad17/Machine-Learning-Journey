#-------------Linear Search--------------#

def LinearSearch(NumberList,NumberToFind):
    for index,value in enumerate(NumberList):
        if value == NumberToFind:
            return index & "Data Found"
    return "Data Not Found"
    
listOfNumber = [1,4,2,5,7,3,6]
x = LinearSearch(listOfNumber,10)
print(f"Linear search value : ",x)



#-----------Binary Search------------#


def BinarySearch(NumberList,NumberToFind):
    left = 0
    right = len(NumberList) - 1
    mid = 0
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = NumberList[mid]
        if NumberToFind == mid_value:
            return mid
        
        if NumberToFind > mid_value:
            left = mid + 1
        else:
            right = mid -1
        
    return "Data Not Found"

x = [12,34,45,67,78,89,99,909]
y = BinarySearch(x,5)
print("Binary search value : ",y)



#--------------Recursive Binary Search-----------


def RecursiveBinarySearch(NumberList,NumberToFind,left,right):
    if right < left:
        return -1
    
    mid = (left + right) //2
    if mid >= len(NumberList) or mid <0:
        return -1
    
    mid_number = NumberList[mid]
    
    if mid_number == NumberToFind:
        return mid
    if mid_number < NumberToFind:
        return RecursiveBinarySearch(NumberList,NumberToFind,mid+1,right)
    else:
        return RecursiveBinarySearch(NumberList,NumberToFind,left,mid-1)
        
    


num_list = [12,13,14,15,17,18,20]
z = RecursiveBinarySearch(num_list,12,0,len(num_list))
print("Recursive Binary Search value: ",z)        

        




