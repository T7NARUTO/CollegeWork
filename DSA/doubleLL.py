class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def __str__(self):
        cur = self.head
        result = ""
        while cur is not None:
            result = result + str(cur.value) + "<->"
            cur = cur.next
        return result[:-3]

    def __getitem__(self, item):
        if item > self.n:
            return IndexError("out of range")
        cur = self.head
        for _ in range(item):
            cur = cur.next
        return cur.value

    def __len__(self):
        return self.n

    def insertHead(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
            self.n += 1
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.n += 1

    def insertTail(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head, self.tail = new_node, new_node
            self.n += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insertAfter(self, prev_value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            return "Empty Double LL"
        cur = self.head
        while cur is not None:
            if cur.value == prev_value:
                new_node.next = cur.next
                new_node.prev = cur
                cur.next = new_node
                self.n += 1
                return
            cur = cur.next
        return "Error"

    def insertBefore(self, next_value, new_value):
        if self.head is None:
            return "Empty Double LL"
        cur = self.head
        new_node = Node(new_value)
        while cur is not None:
            if cur.value == next_value:
                new_node.prev = cur.prev
                new_node.next = cur
                if cur.prev is None:
                    self.head = new_node
                else:
                    cur.prev.next = new_node
                self.n += 1
                return
            cur = cur.next
        
    def del_Head(self):
        if self.head is None:
            raise InterruptedError("Empty Linked List")
        self.head = self.head.next
        self.head.prev = None
        self.n -= 1
    
    def del_Tail(self):
        self.tail = self.tail.prev
        self.tail.next = None
        self.n -= 1

dll = DLL()
dll.insertHead(10)
dll.insertTail(20)
dll.insertHead(30)
dll.insertAfter(30, 15)
dll.insertBefore(30, 1)
print(dll)
print(len(dll))
print(dll[4])
