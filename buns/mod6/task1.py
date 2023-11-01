class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, value):
        if self.end == None:
            self.start = Node(value)
            self.end = self.start
        else:
            node = Node(value)
            self.end.next = node
            self.end = node
        self.size += 1

    def get(self, index, returnNode=False):
        if index < 1 or index > self.size:
            raise Exception("IllegalArgumentException")
        counter = 1
        current_node = self.start
        while counter < index:
            counter += 1
            current_node = current_node.next

        if returnNode:
            return current_node
        return current_node.data

    def remove(self, index):
        if index == 1:
            self.start = self.start.next
        elif index == self.size:
            self.end = self.get(index-1, returnNode=True)
            self.end.next = None
        else:
            prev_node = self.get(index-1, returnNode=True)
            next_node = prev_node.next.next
            prev_node.next = next_node
        self.size -= 1

    def insert(self, index, val):
        node = Node(val)
        if index == 1:
            node.next = self.start
            self.start = node
        else:
            prev_node = self.get(index - 1, returnNode=True)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def __iter__(self):
        self.iterNode = self.start
        return self

    def __next__(self):
        if self.iterNode == None:
            raise StopIteration()
        result = self.iterNode.data
        self.iterNode = self.iterNode.next
        return result