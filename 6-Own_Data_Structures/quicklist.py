class QuickList:
    """ Implement a class QuickList with the following methods:
            move(k): move the first k elements of the list to the end of the list
            get(i): return the element at the index i 

        Solution explanation:
            Aside from setting self.head at the k-th position which is very clear...
            
            The key here is to "wrap around" the list by using the % 
            For example, if we have a list of length 5 and we want to move the first 7 
            elements to the end of the list, we can calculate the new head index as follows: 
            (head + 7) % 5 = 2. This means that we need to move 2 elements to the end of the list, 
            and then "wrap around" to the beginning of the list to get the new head index.

            This treats the list like a "circular buffer", where we can move elements to end of list 
            and then "wrap around" at beginning if we need to...

    """
    def __init__(self, t):
        self.t = t
        self.n = len(t)
        self.head = 0

    def move(self, k):
        self.head = (self.head + k) % self.n

    def get(self, i):
        return self.t[(self.head + i) % self.n]


if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
