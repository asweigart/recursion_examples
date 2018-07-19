class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


Node('Dog', Node('Cat', Node('Rat', None)))