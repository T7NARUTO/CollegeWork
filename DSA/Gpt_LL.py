class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur = self.head
        result = ''
        while cur:
            result += str(cur.data) + '->'
            cur = cur.next
        return result[:-2]

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.size += 1

    def insert_after(self, after_val, new_val):
        if not self.head:
            return "Linked list is empty"
        cur = self.head
        while cur:
            if cur.data == after_val:
                new_node = Node(new_val)
                new_node.next = cur.next
                cur.next = new_node
                self.size += 1
                return
            cur = cur.next
        return f"{after_val} not found in the linked list"

    def pop(self):
        if not self.head:
            return "Linked list is empty"
        if not self.head.next:
            self.head = None
        else:
            cur = self.head
            while cur.next.next:
                cur = cur.next
            cur.next = None
        self.size -= 1

    def remove(self, value):
        if not self.head:
            return "Linked list is empty"
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return
        cur = self.head
        while cur.next:
            if cur.next.data == value:
                cur.next = cur.next.next
                self.size -= 1
                return
            cur = cur.next
        return f"{value} not found in the linked list"

    def del_head(self):
        if not self.head:
            return "Linked list is empty"
        self.head = self.head.next
        self.size -= 1

    def del_tail(self):
        if not self.head:
            return "Linked list is empty"
        if not self.head.next:
            self.head = None
        else:
            cur = self.head
            while cur.next.next:
                cur = cur.next
            cur.next = None
        self.size -= 1

    def del_val(self, value):
        if not self.head:
            return "Linked list is empty"
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return
        cur = self.head
        while cur.next:
            if cur.next.data == value:
                cur.next = cur.next.next
                self.size -= 1
                return
            cur = cur.next
        return f"{value} not found in the linked list"

    def index(self, value):
        pos = 0
        cur = self.head
        while cur:
            if cur.data == value:
                return pos
            pos += 1
            cur = cur.next
        raise ValueError("Element not found in linked list")

    def replace(self, prev_val, new_val):
        cur = self.head
        while cur:
            if cur.data == prev_val:
                cur.data = new_val
                return
            cur = cur.next
        return f"{prev_val} not found in the linked list"


def main():
    ll = None

    while True:
        print('''
        1. Create an empty linked list.
        2. Perform insertion operations.
        3. Perform delete operations.
        4. Search for an element.
        5. Perform update operations.
        6. Exit
        ''')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ll = LinkedList()
            print("Created an empty linked list")
        elif choice == 2:
            print('''
            1. Insert at the head.
            2. Insert at the tail.
            3. Insert after a value.
            ''')
            option = int(input("Enter your choice: "))
            if option == 1:
                val = int(input("Enter the value for the new head: "))
                ll.insert_head(val)
                print("Inserted at the head successfully")
            elif option == 2:
                val = int(input("Enter the value for the new tail: "))
                ll.insert_tail(val)
                print("Inserted at the tail successfully")
            elif option == 3:
                after_val = int(input("Enter the value after which you want to insert: "))
                new_val = int(input("Enter the new value: "))
                ll.insert_after(after_val, new_val)
                print("Inserted after the value successfully")
            else:
                print("Invalid option")
        elif choice == 3:
            print('''
            1. Delete the head.
            2. Delete the tail.
            3. Delete a value.
            ''')
            option = int(input("Enter your choice: "))
            if option == 1:
                ll.del_head()
                print("Deleted the head successfully")
            elif option == 2:
                ll.del_tail()
                print("Deleted the tail successfully")
            elif option == 3:
                val = int(input("Enter the value to be deleted: "))
                ll.del_val(val)
                print("Deleted the value successfully")
            else:
                print("Invalid option")
        elif choice == 4:
            print('''
            1. Search for a value.
            2. Get value using index.
            ''')
            option = int(input("Enter your choice: "))
            if option == 1:
                val = int(input("Enter the value to be searched: "))
                try:
                    pos = ll.index(val)
                    print(f"Element found at position {pos}")
                except ValueError:
                    print("Element not found in linked list")
            elif option == 2:
                ind = int(input("Enter the index number: "))
                try:
                    value = ll[ind]
                    print(f"Value at index {ind} is {value}")
                except IndexError:
                    print("Index out of range")
            else:
                print("Invalid option")
        elif choice == 5:
            print('''
            1. Replace a value.
            ''')
            option = int(input("Enter your choice: "))
            if option == 1:
                prev_val = int(input("Enter the value to be replaced: "))
                new_val = int(input("Enter the new value: "))
                ll.replace(prev_val, new_val)
                print