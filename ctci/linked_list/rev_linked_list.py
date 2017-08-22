class Node :
    def __init__(self, name):
        self.val = name
        self.Next = None

class LinkedList :
    def __init__ (self) :
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None) :
            curNext = current.Next
            current.next = prev
            prev = current
            current = curNext
        self.head = prev
