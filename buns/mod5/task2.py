class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            raise Exception("Queue is empty")
        
        val = self.start.data
        if self.start.next is None:
            self.start = None
            return val
        self.start = self.start.next
        return val

    def push(self, val):
        if self.start is None:
            self.start = Node(None)
            self.start.data = val
            self.end = self.start
        else:
            node = Node(val)
            node.prev = self.end
            self.end.next = node
            self.end = node

    def insert(self, n, val):
        current_node = self.start
        counter = 0

        while counter != n-1:
            if current_node is None:
                raise Exception("IllegalArgumentException")
            counter += 1
            current_node = current_node.next

        node = Node(val)
        node.prev = current_node
        node.next = current_node.next
        current_node.next.prev = node
        current_node.next = node

    def print(self):
        node = self.start
        if node is None:
            print(None)
        else:
            values = []
            while node.next is not None:
                values.append(node.data)
                node = node.next
            values.append(node.data)
            print(values)