class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.n = 0

    def __str__(self):
        cur = self.head
        result = ''
        while cur is not None:
            result = result + str(cur.data) + '->'
            cur = cur.next
        return result[:-2]

    def __len__(self):
        return self.n

    def insert_head(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.n += 1
            return
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
            self.n += 1

    def insert_tail(self,value):
        new_node = Node(value)
        cur = self.head
        if self.head == None:
            self.head = new_node
        while cur is not None:
            if cur.next is None:
                cur.next = new_node
                self.n += 1
                return
            cur = cur.next
        return "Error"

    def pop(self):
        cur = self.head
        if cur == None:
            return "empty ll"
        if cur.next == None:
            self.head = None
        while cur is not None:
            if cur.next.next is None:
                cur.next = None
                self.n -= 1
                return
            cur = cur.next

    def remove(self,value):
        cur = self.head
        if cur.data == value:
            self.head = cur.next
            return
        while cur.next is not None:
            if cur.next.data == value:
                break
            cur = cur.next
        return 'value not in ll'
ll = LL()
l = [1,12,13,14,15,16,17,18,19,20]
ll.insert_tail(11)
ll.insert_tail(12)
ll.remove(12)
print(ll)