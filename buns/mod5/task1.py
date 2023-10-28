class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end == None:
            raise Exception("Stack is empty")
        
        val = self.end
        self.end = self.end.prev
        return val

    def push(self, val):
        if self.end is None:
            self.end = Node(val)
        else:
            node = Node(val)
            node.prev = self.end
            self.end = node

    def print(self):
        if self.end is None:
            raise Exception("Stack is empty")
        
        node = self.end
        nodes_data = []

        while node.prev is not None:
            nodes_data.append(node.data)
            node = node.prev

        nodes_data.append(node.data)
        print(nodes_data[::-1])

stack = Stack()
stack.print()