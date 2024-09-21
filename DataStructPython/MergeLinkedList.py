class Node:

    def __init__(self,value):
        self.val = value 
        self.next = None 
        

class SingleLinkedList:

    def __init__(self):
        self.start = None
    
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :   ")
            p = self.start 
            while p is not None:
                print(p.val , " ", end='')
                p = p.next 
            print()
   
    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp


    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)
    

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.next:

            p = self.start
            while  p.next != end:
                q = p.next 
                if p.val > q.val:
                    p.val,q.val = q.val,p.val 
                p = p.next     
            end = p

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list
    
    def _merge1(self, p1, p2):
        if p1.val <= p2.val:
            startNew = Node(p1.val)
            p1 = p1.next
        else:
            startNew = Node(p2.val)
            p2 = p2.next

        pN = startNew

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                pN.next = Node(p1.val)
                p1 = p1.next
            else:
                pN.next = Node(p2.val)
                p2 = p2.next
            pN = pN.next
        
        while p1 is not None:
            pN.next = Node(p1.val)
            p1 = p1.next
            pN = pN.next
        
        while p2 is not None:
            pN.next = Node(p2.val)
            p2 = p2.next
            pN = pN.next
        
        return startNew

        
    def merge2(self,list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list
        
    def _merge2(self, p1, p2):
        if p1.val <= p2.val:
            startMerge = p1
            p1 = p1.next
        else:
            startMerge = p2
            p2 = p2.next

        pM = startMerge

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                pM.next = p1
                p1 = p1.next
            else:
                pM.next = p2
                p2 = p2.next
            
            pM = pM.next

        if p1 is None:
            pM.next = p2
        else:
            pM.next = p1

        return startMerge
        

#########################################################################################

list1 = SingleLinkedList()
list2 = SingleLinkedList()

list1.create_list() 
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()
	
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()

list3 = list1.merge1(list2)
print("Merged List Values- "); list3.display_list()
		
print("First List - "); list1.display_list()
print("Second List - "); list2.display_list()
		
list3 = list1.merge2(list2)
print("Merged List Links- "); list3.display_list()
print("First List - ");  list1.display_list()
print("Second List - "); list2.display_list()