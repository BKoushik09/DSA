#INSERTION & DELETION
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def delete(value):
    global head
    temp = head
    if temp and temp.data == value:
        head = temp.next
        return 
    prev = None
    while temp and temp.data != value:
        prev = temp
        temp = temp.next
    if temp is None:
        print("Value not in Linkedlist")
        return
    prev.next = temp.next
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
n = int(input("enter number of nodes:"))
for i in range(n):
    data = int(input("enter value:"))
    insert(data)
print("Inserted Linkedlist")
display()
key = int(input("enter value to delete:"))
delete(key)
print("Updated linkedlist after deletion")
display()'''

#SEARCHING
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def search(key):
    temp = head
    position = 1
    while temp:
        if temp.data == key:
            print("element found in node:", position)
            return
        temp = temp.next
        position += 1
    print("no node reflects the key")
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
n = int(input("enter number of nodes:"))
for i in range(n):
    data = int(input("enter value:"))
    insert(data)
print("Inserted Linkedlist")
display()
key = int(input("enter value to search:"))
search(key)'''

#REVERSING A LINKEDLIST
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def reverse():
    global head
    prev = None
    current = head
    while current:
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
    head = prev
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
n = int(input("enter number of nodes:"))
for i in range(n):
    data = int(input("enter value:"))
    insert(data)
print("Inserted Linkedlist")
display()
reverse()
print("Reversed linkedlist")
display()'''

#REPLACING A VALUE IN A LINKEDLIST
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = next
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def replace(old, new):
    temp = head
    found = False
    while temp:
        if temp.data == old:
            temp.data = new
            found = True
        temp = temp.next
    if found:
        print("Replaced", old, "with", new)
    else:
        print("Value", old, "not found in the linked list")
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
n = int(input("enter number of nodes:"))
for i in range(n):
    data = int(input("enter value:"))
    insert(data)
print("Inserted Linkedlist")
display()
old = int(input("enter value to be replaced:"))
new = int(input("enter new value:"))
replace(old, new)
print("Updated linkedlist after replacement")
display()'''

#DETECTING A CYCLE IN A LINKEDLIST
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert_end(data):
    global head
    newnode = node(data)
    if head is None:
        head = newnode
        return
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
def create_cycle(pos):
    global head
    if pos == -1:
        return
    temp = head
    cycle_node = None
    index = 0
    while temp.next:
        if index == pos:
            cycle_node = temp
        temp = temp.next
        index += 1
    if cycle_node:
        temp.next = cycle_node
def detect_cycle():
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return
    print("No cycle detected")
def display(limit=15):
    temp = head
    count = 0
    while temp and count < limit:
        print(temp.data, end="->")
        temp = temp.next
        count += 1
    if temp:
        print("...")
    else:
        print("None")
n = int(input("enter number of nodes:"))
for i in range(n):
    data = int(input("enter value:"))
    insert_end(data)
print("Inserted Linkedlist")
display()
pos = int(input("enter position to create cycle (-1 for no cycle):"))
create_cycle(pos)
detect_cycle()
