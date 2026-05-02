#DOUBLE LINKEDLIST INSERTIONS(AT BEGIN, END, POSITION)

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
head = None
def insert_begin(head, data):
    newnode = node(data)
    if head:
        head.prev = newnode
        newnode.next = head
    return newnode
def insert_end(head, data):
    newnode = node(data)
    if head is None:
        return newnode
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
    newnode.prev = temp
    return head
def insert_pos(head, data, pos):
    newnode = node(data)
    if pos == 1:
        if head:
            head.prev = newnode
            newnode.next = head
        return newnode
    temp = head
    for _ in range(pos - 2):
        temp = temp.next
    newnode.next = temp.next
    if temp.next:
        temp.next.prev = newnode
    temp.next = newnode
    newnode.prev = temp
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end="<->")
        temp = temp.next
    print("None")'''

#n = int(input("enter number of nodes:"))
'''for i in range(n):
    data = int(input("enter value:"))
    head = insert_begin(head, data)
print("Inserted Linkedlist at begin")
display(head)'''

'''for i in range(n):
    data = int(input("enter value:"))
    head = insert_end(head, data)
print("Inserted Linkedlist at end")
display(head)'''

'''for _ in range(n):
    data = int(input("enter value:"))
    head = insert_pos(head, data, _ + 1)
pos = int(input("enter position to insert:"))
data = int(input("enter value:"))
head = insert_pos(head, data, pos)
display(head)'''

#DOUBLE LINKEDLIST DELETION(BEGIN, END)
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_begin(head):
    if head is None:
        return None
    head = head.next
    if head:
        head.prev = None
    return head
def delete_end(head):
    if head is None:
        return None
    temp = head
    if temp.next is None:
        return None
    while temp.next:
        temp = temp.next
    temp.prev.next = None
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end = "<->")
        temp = temp.next
    print("None")
head = None
n = int(input("enter the number of nodes:"))

for _ in range(n):
    val = int(input("enter value:"))
    new = node(val)
    new.next = head
    if head:
        head.prev = new
    head = new
display(head)'''
'''head = delete_begin(head)
display(head)'''

'''head = delete_end(head)
display(head)'''


#DELETE VALUE BY POSITION
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def delete_value(head, key):
    temp = head
    while temp:
        if temp.data == key:
            if temp.prev == None:
                head = temp.next
                if head:
                    head.prev = None
                    return head
            if temp.next == None:
                temp.prev.next = None
                return head
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        temp = temp.next
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end = "<->")
        temp = temp.next
head = None
n = int(input("enter the number of nodes:"))
for _ in range(n):
    val = int(input("enter value:"))
    if head is None:
        head = node(val)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        new = node(val)
        temp.next = new
        new.prev = temp
key = int(input("enter the value to be deleted:"))
head = delete_value(head, key)
display(head)'''


#SEARCHING IN DOUBLE LINKEDLIST
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def search(head, key):
    temp = head
    pos = 1
    while temp:
        if temp.data == key:
            return pos
        temp = temp.next
        pos += 1
    return -1
head = None
n = int(input("enter the number of nodes:"))
for _ in range(n):
    val = int(input("enter value:"))
    if head is None:
        head = node(val)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        new = node(val)
        temp.next = new
        new.prev = temp
key = int(input("enter value to search:"))
pos = search(head, key)
if pos != -1:
    print(key, "found at node", pos)
else:
    print('Not found')

