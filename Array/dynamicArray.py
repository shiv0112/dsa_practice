"""
Concept : Dynamic Array
This is a class that makes a list like data structure using arrays from scratch
it will have functionalities like:
Create
len
append
print
indexing
pop
clear
find
insert
delete
remove
"""

import ctypes

class meraList:
    def __init__(self):
        self.size = 1 # stores the current size allocated
        self.n = 0 # stores the current size occupied
        # create a c type array with size = self.size
        self.A = self.__make_array(self.size)

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)() # creates a C type array(static, referential) with size capacity
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        res = ''
        for i in range(self.n):
            res += str(self.A[i]) + ','
        return '['+res[:-1]+']'
    
    def __getitem__(self,index):
        if 0 <= index <= self.n:
            return self.A[index]
        else:
            print("IndexError: Index out of bounds")

    def __resize(self, size):
        B = self.__make_array(size)
        self.size = size
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __delitem__(self, pos):
        if 0 <= pos <= self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n - 1
        else:
            print("Index out of range")
        
    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size * 2)
        
        # append 
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'
        
        print(self.A[self.n - 1])
        self.n -= 1 

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return f'{item} not found in the list'
    
    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n += 1

    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos





