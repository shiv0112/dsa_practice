import ctypes

class myList:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A  = self.__make_array(self.size) 

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n

    def __resize(self):
        self.size = self.size + 8 
        B = self.__make_array(self.size)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __str__(self):
        if self.n == 0:
            return "[]"
        
        res = ""
        for i in range(self.n):
            res += str(self.A[i]) + ','
        return '[' + res[:-1] + ']'
    
    def __getitem__(self, pos):
        if isinstance(pos, slice):
            res = ''

            print(pos.start, pos.stop, pos.step)

            start, stop, step = pos.start or 0, pos.stop or self.n, pos.step or 1

            # Adjusting start and stop for negative values
            start = start + self.n if start < 0 else start
            stop = stop + self.n if stop < 0 else stop

            # Adjusting start and stop for step < 0
            if step < 0:
                start, stop = stop - 1, start - 1


            print(start, stop, step)

            for i in range(start, stop, step):
                print(i)
                res += str(self.A[i]) + ','
            return '[' + res[:-1] + ']'
        
        if pos < 0:
            pos = self.n + pos 

        return self.A[pos]
    
    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -=1
        else:
            print("IndexError")

    def append(self, item):
        if self.size == self.n:
            self.__resize()
        
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        print(self.A[self.n-1])
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "IndexError - No item found in the list"
    
    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize()
        for i in range(self.n , pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n += 1

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            print(pos)

    def sorted(self):
        # selection_sort
        for i in range(self.n):
            min = self.A[i]
            pos = i
            for j in range(i+1, self.n):
                if (self.A[j]<min):
                    min = self.A[j]
                    pos = j
            self.A[i], self.A[pos] = self.A[pos], self.A[i]
    
    def min(self):
        m = self.A[0]
        for i in range(self.n):
            if m > self.A[i]:
                m = self.A[i] 
        return m
    
    def max(self):
        m = self.A[0]
        for i in range(self.n):
            if m < self.A[i]:
                m = self.A[i] 
        return m
    
    def sum(self):
        s = 0
        for i in range(self.n):
            s += self.A[i]
        return s
    
    def extends(self, k):
        self.size += k.size
        C = self.__make_array(self.size)
        for i in range(self.n):
            C[i] = self.A[i] 
        for i in range(self.n, self.n+k.n):
            C[i] = k[i - self.n]
        self.n = self.n+k.n
        self.A = C
        


            
