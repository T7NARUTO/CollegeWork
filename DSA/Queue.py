class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            return
        current = self.front
        while current is not None:
            if current.next is None:
                current.next = new_node
                new_node.prev = current
                self.rear = new_node
                return
            current = current.next

    def deQueue(self):
        if self.front is None:
            raise IndexError("queue is empty")
        self.front = self.front.next


q = Queue()
q.enQueue(10)
q.enQueue(11)
q.enQueue(1)
print(q.rear.prev.value)