from Algorithms.Models.Node_S import Node_S

class Stack: #LIFO
    def __init__(self):
        # Init stack
        self.top = None
        self.size = 0
    def push(self, data):
        # Push or insert nodes to stack
        node = Node_S(data, self.top)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1
    def pop(self):
        # Pop or delete nodes to stack
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return False
    def peek(self):
        # Retorn the head node
        return self.top.data if self.top else False
    def clear(self):
        # Clear all stack
        while self.top:
            self.pop()
    def search_element(self, data):
        if self.top:
            current = self.top
            while current:
                if current.data == data:
                    return (f'Elemet {data} founded')
                current = current.next
            return (f'Elemet {data} not founded')