class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.start = None
        #In leetcode head is the same thing as self.start

    def display_list(self):
        pointer = self.start
        if self.start is None:
            print('List is empty')
        else:
            while pointer is not None:
                print('Value: ', pointer.val)
                # print('Pointer: ', pointer)
                # print('next/Next: ', pointer.next)
                pointer = pointer.next
            print()

    def count_nodes(self):
        pointer = self.start
        node_count = 0
        while pointer is not None:
            node_count += 1
            pointer = pointer.next
        print('Number of nodes in the list is ', node_count)


    def search(self, x):
        position = 0
        pointer = self.start
        while pointer is not None:
            if pointer.val == x:
                print(x, 'is at position ', position)
                return True
            pointer = pointer.next
            position += 1
        print(x, ' Not found in list')
        return False
    
    #

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        pointer = self.start
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = temp

    def create_list(self):
        n = int(input('Number of Nodes: '))
        if n <= 0:
            print('Nodes less than or equal to 0, cannot create list.')
            return
        
        for i in range(n):
            data = int(input('Enter the number to be inserted: '))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start

        while p is not None:
            if p.val == x:
                break
            p = p.next

        if p is None:
            print('Data point not found in list')
        else:
            temp = Node(data)
            temp.next = p.next
            p.next = temp

    def insert_before(self, data, x):
        p = self.start
        temp = Node(data)

        if self.start is None:
            print("List is empty")
            return

        if self.start.val == x:
            temp.next = self.start
            self.start = temp
            return

        while p.next is not None:
            if p.next.val == x:
                break
            p = p.next
        
        if p.next is None:
            print(x, "is not in the list")
        else:
            temp.next = p.next
            p.next = temp


    def insert_at_position(self, data, k):
        p = self.start
        i = 0
        if i == k:
            temp = Node(data)
            temp.next = self.start
            self.start = temp
            return
        
        while i >= k and p.next is not None:
            i += 1
            if i == k:
                break
            p = p.next

        if i == k:
            temp = Node(data)
            temp.next = p.next
            p.next = temp
        else:
            print('Position not found in list')

    
    def delete_first_node(self):
        if self.start is None:
            print('List is empty')
            return
        
        self.start = self.start.next

    def delete_last_node(self):
        if self.start is None:
            print('List is empty')
            return
        
        if self.start.next is None:
            self.start = None
            return
        
        p = self.start

        while p.next.next is not None:
            p = p.next
        p.next = None
        

    def delete_node(self, x):
        if not self.start:
            print('List is empty')
            return

        if self.start.val == x:
            self.start = self.start.next
            return
        
        p = self.start
        while p.next is not None:
            if p.next.val == x:
                break
            p = p.next

        if p.next is None:
            print('Item', x ,'not found in list')
        else: 
            p.next = p.next.next
        
    
    def reverse_list(self):
        prev = None
        curr = self.start
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.start = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.next:
            p = self.start
            while p.next != end:
                q = p.next
                if p.val > q.val:
                    p.val, q.val = q.val, p.val
                p = p.next
            end = p


    def bubble_sort_exnexts(self):
        end = None
        while end != self.start.next:
            p = self.start
            r = None
            while p.next != end:
                q = p.next
                if p.val > q.val:
                    p.next = q.next
                    q.next = p
                    if r is not None:
                        r.next = q
                    else:
                        self.start = q
                    p,q = q,p
                r = p  
                p = p.next
            end = p


    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True
        
    def find_cycle(self):
        if self.start is None or self.start.next is None:
            return None
        
        slow = self.start
        fast = self.start

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        
        return None

        

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

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

    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)

    def _merge_sort_rec(self, list_start):
        if list_start is None or list_start.next is None:
            return list_start
        
        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(start1, start2)

        return startM

    def _divide_list(self, p):
        q = p.next.next

        while q is not None and q.next is not None:
            p = p.next
            q = q.next.next
        
        start2 = p.next
        p.next = None
        return start2


#############################################################################################################

list = SingleLinkedList() 

list.create_list() 

while True:
    print("1.Display list") 
    print("2.Count the number of nodes") 
    print("3.Search for an element")
    print("4.Insert in empty list/Insert in beginning of the list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging nexts")
    print("15.MergeSort")
    print("16.Insert Cycle")
    print("17.Detect Cycle")
    print("18.Remove cycle")
    print("19.Quit")
        
    option = int(input("Enter your choice : " ))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which to insert : ")) 
        list.insert_after(data,x)
    elif option == 7:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which to insert : ")) 
        list.insert_before(data,x)
    elif option == 8:
        data = int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which to insert : ")) 
        list.insert_at_position(data,k)
    elif option == 9:
        list.delete_first_node() 
    elif option == 10:
        list.delete_last_node() 
    elif option == 11:
        data = int(input("Enter the element to be deleted : ")) 
        list.delete_node(data)             
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata() 
    elif option == 14:
        list.bubble_sort_exnexts() 
    elif option == 15:
        list.merge_sort() 
    elif option == 16:
        data = int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(data) 
    elif option == 17:
        if list.has_cycle():
            print("List has a cycle")
        else:
            print("List does not have a cycle") 
    elif option == 18:
        list.remove_cycle() 
    elif option == 19:
        break
    else:
        print("Wrong option") 
    print() 
