class Node :
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self):
        self.head =None
        
    def print(self):
        if self.head ==None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) +" --> " if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count 
        
    def AddBeginning(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def AddEnd(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
        
    def InsertAnyPos(self,index,data):
        if index <0 or index>self.get_length():
            print("Invalid Index")
            return 
            
        if index == 0:
            self.AddBeginning(data)
            return 
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    
    
    def RemoveAnyPos(self,index):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")
            return
            
        if index == 0:
            self.head = self.head.next 
            return 
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    
    def InsertList(self,data_list):
        self.head = None
        for data in data_list:
            self.AddEnd(data)        
            
  
if __name__ =='__main__':
    l1 = LinkedList()
    # l1.AddBeginning(5)
    # l1.AddBeginning(4)
    # l1.AddBeginning(3)
    # l1.AddEnd(7)
    # l1.AddEnd(8)
    # l1.InsertAnyPos(0,24)
    # l1.RemoveAnyPos(2)
    l1.InsertList([1,2,3,4,5])
    l1.AddEnd(12)
    l1.print()    