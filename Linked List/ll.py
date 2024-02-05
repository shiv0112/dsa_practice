class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n    
    
    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + " --> "
            curr = curr.next
        return result[:-5]
    
    def __getitem__(self, pos):
        curr = self.head
        index = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            index += 1
        return "Index not present"

    
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1
        print(self)

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next 
        curr.next = new_node
        self.n += 1
        print(self)

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
            print(self)
        else:
            return "Item not found"
    
    def clear(self):
        self.head = 0
        self.n = 0

    def del_head(self):
        if self.head == None:
            return 'Empty Linked List'
        self.head = self.head.next
        self.n -= 1
        print(self)
    
    def pop(self):
        
        curr = self.head

        if curr == None:
            return 'Empty Linked List'

        if curr.next == None:
            return self.del_head()
        
        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n -= 1
        print(self)

    def remove(self, value):
        curr = self.head
        
        if curr.data == value:
            return self.del_head()
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            return 'Not Found'
        else:
            curr.next = curr.next.next
            self.n-=1
            print(self)

    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return "Not Found"
    
    
        

        
