class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        if self.top is not None:
            self.top.next = new_node
        new_node.prev = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        self.top = self.top.prev

    def clear(self):
        self.top = None

    def peek(self):
        return print(self.top.value)

    def is_empty(self):
        return self.top is None

    def __len__(self):
        current = self.top
        size = 0
        while current:
            size += 1
            current = current.next
        return size


st = Stack()
st.push(10)
st.push(11)
st.pop()
st.peek()
