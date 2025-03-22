class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def addNode(self, node):
        if self.length == 0:
            self.head = node
        elif self.length == 1:
            self.head.next = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        self.length += 1

    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

list = LinkedList()

list.addNode(Node(12))
list.addNode(Node(24))
list.addNode(Node(5))
list.addNode(Node(32))
list.addNode(Node(18))

print("===== print =====")
list.printList()