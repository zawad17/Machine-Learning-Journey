def bubble_sort(elements):
    size = len(elements)
    for i in range(size -1):
        swapped = False
        for j in range(size -1 -i):
            if elements[j] > elements[j+1]:
                temp = elements[j]  # Here swap function is not work. they passed by value not passed by reference
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped :
            break
        
if __name__ == "__main__":
    element_list = [5,7,9,12,5,4,9,1,6]
    element_list1 = [1,2,3,4,5,6,7,8,9]
    element_list2 = [9,8,7,6,5,4,3,2,1]
    bubble_sort(element_list)
    bubble_sort(element_list1)             
    bubble_sort(element_list2)
    print(element_list)
    print(element_list1)
    print(element_list2)
    
    