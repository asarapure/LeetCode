class Node :
    def __init__(self, val):
        self.data = val
        self.Next = None


class LinkedList :
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head == None :
            self.head = Node(val)

        else :
            current = self.head
            while (current.Next) :
                current = current.Next
            current.Next = Node(val)

    def printLinkedList(self):
        ll_list = []
        if self.head == None :
            return ll_list
        else :
            current = self.head
            while current :
                ll_list.append(current.data)
                current = current.Next
            return ll_list

ll = LinkedList()
n = Node(3)

print(ll.printLinkedList())
ll.add(n.data)
print(ll.printLinkedList())
ll.add(Node(55).data)
print(ll.printLinkedList())

