#INSERT AT BEGIN 
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new = node(data)
    if head is None:
        new.next = new
        return new
    temp = head
    while temp.next != head:
        temp = temp.next
    new.next = head
    temp.next = new
    head = new
    return head
def insert_end(head, data):
    new = node(data)
    if head is None:
        new.next = new
        return new
    temp = head
    while temp.next != head:
        temp = temp.next
    temp.next = new
    new.next = head
    return head
def display(head):
    if head is None:
        return
    temp = head
    while True:
    #while temp.next != next: (for begin)
        print(temp.data, end = "->")
        temp = temp.next
        if temp == head:
            print(temp.data)
            break
head = None
n = int(input("enter the number of nodes:"))
for _ in range(n):
    val = int(input("enter value:"))
    #head = insert_begin(head, val)
    head = insert_end(head, val)
display(head)