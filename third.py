class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isempty(self):
        return self.head == None

    def append(self, node):
        if self.isempty():
            self.head = node
        elif self.length == 1:
            self.head.next = node
        else:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = node
        self.length += 1