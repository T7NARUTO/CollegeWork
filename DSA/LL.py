class Node:
    def __init__(self, value):
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

    def __getitem__(self, item):
        pos = 0
        cur = self.head
        if item > self.n:
            return "invalid index"
        while cur is not None:
            if pos == item:
                return cur.data
            pos += 1
            cur = cur.next

    def insert_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.n += 1
            return
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
            self.n += 1

    def insert_tail(self, value):
        new_node = Node(value)
        cur = self.head
        if self.head is None:
            self.head = new_node
        while cur is not None:
            if cur.next is None:
                cur.next = new_node
                self.n += 1
                return
            cur = cur.next
        return "Error"
        
    def insert_after(self,after_val,new_val):
      if self.head is None:
        return "empty Linked List"
      new_node = Node(new_val)
      cur = self.head
      while cur is not None:
        if cur.data == after_val:
          new_node.next = cur.next
          cur.next = new_node
          self.n += 1
          return
        cur = cur.next
      return f"{after_val} not found in Linked List"
      
          
    def pop(self):
        cur = self.head
        if cur is None:
            return "empty ll"
        if cur.next is None:
            self.head = None
        while cur is not None:
            if cur.next.next is None:
                cur.next = None
                self.n -= 1
                return
            cur = cur.next

    def remove(self, value):
        cur = self.head
        if cur.data == value:
            self.head = cur.next
            return
        while cur is not None:
            if cur.next.data == value:
                if cur.next.next is None:
                    cur.next = None
                    self.n -= 1
                    return
                cur.next = cur.next.next
                self.n -= 1
                return
            cur = cur.next
        return 'value not in ll'

    def del_head(self):
        cur = self.head
        if cur is None:
            return "empty LL"
        if cur.next is None:
            self.head = None
            self.n -= 1
            return
        self.head = cur.next
        self.n -= 1

    def del_tail(self):
        cur = self.head
        if cur is None:
            return "empty LL"
        if cur.next is None:
            self.head = None
            return
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None
        self.n -= 1

    def del_val(self,value):
      if self.head is None:
        return "Linked List is empty "
      cur = self.head
      while cur is not None:
        if cur.next.data == value:
          cur.next = cur.next.next.next
          self.n -= 1
          return
        cur = cur.next
      return "value not found"

    def index(self, value):
        pos = 0
        cur = self.head
        while cur is not None:
            if cur.data == value:
                return pos
            pos += 1
            cur = cur.next
        raise Element_not_found:("Element not found in Linked List")

    def replace(self, prev_val, new_val):
        cur = self.head
        while cur is not None:
            if cur.data == prev_val:
                cur.data = new_val
                return
            cur = cur.next
        return "value not found"


while True:
  choice = int(input ('''
  1.Create a Empty Linked List.
  2.Perform Insertion Operations.
  3.Perform Delete Operations.
  4.Search a Element.
  5.Perform Update Operations.
  6.Exit
  ''')
  if choice == 1:
    ll = LL()
    print("Created a Empty Linked list")
    continue
  elif choice == 2:
    option = int(input("
        1.Insert Head.
        2.Insert Tail.
        3.Insert after a value.
    "))
    if option == 1:
      val = int(input("Enter the value of the new head. "))
      try:
        ll.insert_head(value)
        print("Insert Head operation successful ")
       except Exception as e:
         print("you cannot insert head untill you create a Linked List ")
    elif option == 2:
      val = int(input("Enter the value of the new Tail. "))
      try:
        ll.insert_tail(val)
        print("Insert tail operation successful ")
      except Exception as e:
        print("you cannot insert tail untill you create a Linked List ")
    elif choice == 3:
      after_val = int(input("Enter the value after which you want to enter the new value"))
      new_val = int(input("Enter the new value "))
      try:
        ll.insert_after(after_val,new_val)
        print("Insert after operation sucessful ")
      except Exception as e:
        print("you cannot perform this operation untill you create a linked list")
    else:
      print("Invalid option")
    continue
  elif choice == 3:
    option = int(input("
      1.Delete Head.
      2.Delete Tail.
      3.Delete value.
    "))
    if option == 1:
      try:
        ll.del_head()
        print("Delete Head operation successful ")
      except Exception as e:
        print("You need to create a Linked List to perform this operation ")
    elif option == 2:
      try:
        ll.del_tail()
        print("Delete Tail operation successful ")
      except Exception as e:
        print("You need to create a Linked List to perform this operation ")
    elif option == 3:
      val = int(input("Enter the the value you want to delete"))
      try:
        ll.del_val(val)
        print("Deleted the value successfully ")
      except Exception as e:
        print("You need to create a Linked list to perform this operation ")
    else:
      print("invalid option")
    continue
  elif choice == 4:
    option = int(input("
      1.Search value.
      2.Get value using Index number.
    "))
    if option == 1:
      val = int(input("Enter the value to be searched "))
      try:
        pos = ll.index(val)
        print(f"Element found at {pos}")
      except Exception as e:
        print(e)
    elif option == 2:
      ind = int(input("Enter the Index number"))
      try:
        ll[ind]
      except Exception as e:
        print(e)
    else:
      print("invalid option")
    continue
  elif choice == 5:

      # Tab to edit