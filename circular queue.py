class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    def enqueue(self, value):
        if self.is_full():
            print("Queue overflow!!!cannot insert value:", value)
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print("Inserted value:", value)
    def dequeue(self):
        if self.is_empty():
            print("queue underflow!! nothing to delete")
            return 
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.rear+1) % self.size
        print("Deleted:", removed)
    def peek(self):
        if self.is_empty():
            print("Queue empty...")
        else:
            print("front element:", self.queue[self.front])
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end = ' ')
            if i == self.rear:
                break
            i = (i+1) % self.size
        print()
size = int(input("enter the size of circular queue:"))
cq = CircularQueue(size)
while True:
    print("\n 1. Enqueue\n2. Dequeue\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("enter choice:"))
    if choice == 1:
        val = int(input("enter value to insert:"))
        cq.enqueue(val)
    elif choice == 2:
        cq.dequeue()
    elif choice == 3:
        cq.peek()
    elif choice == 4:
        cq.display()
    elif choice == 5:
        print("exiting...")
        break
    else:
        print("invalid choice")