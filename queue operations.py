#ENQUEUE OPERATION
'''queue = []
n = int(input("enter the size of the queue:"))
for i in range(n):
    val = int(input("enter value:"))
    queue.append(val)
print("queue after enqueue:", queue)'''


#DEQUEUE OPERATION
'''queue = list(map(int, input("enter the queue elements:").split()))
if len(queue) == 0:
    print("queue is empty...underflow")
else:
    removed = queue.pop(0)
    print("dequeue element:", removed)
    print("remaining elements:", queue)
    print("peek element:", queue[0])
    print("size of queue:", len(queue))'''

#ENQUEUE USING LINKED LIST
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("enter the size of the queue:"))
for i in range(n):
    val = int(input("enter the value:"))
    new = node(val)
    if front is None:
        front = rear = new
    else:
        rear.next = new
        rear = new
temp = front
print("queue after enqueue:", end = " ")
while temp:
    print(temp.data, end = ' ')
    temp  = temp.next'''

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("enter the size of the queue:"))
for i in range(n):
    val = int(input("enter the value:"))
    new = node(val)
    if front is None:
        front = rear = new
    else:
        rear.next = new
        rear = new
if front is None:
    print("queue is empty...underflow")
else:
    print("peek element:", front.data)'''


'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("enter the size of the queue:"))
for i in range(n):
    val = int(input("enter the value:"))
    new = node(val)
    if front is None:
        front = rear = new
    else:
        rear.next = new
        rear = new
if front is None:
    print("queue is empty...underflow")
else:
    removed = front.data
    front = front.next
    if front is None:
        rear = None
    print("dequeue element:", removed)
temp = front
print("queue after enqueue:", end = " ")
while temp:
    print(temp.data, end = ' ')
    temp  = temp.next'''