# Program 8 - Queue
from collections import deque

queue = deque()
def enqueue():
    val = input("Enter value to enqueue: ")
    queue.append(val)
def dequeue():
    if queue:
        print("Dequeued:", queue.popleft())
    else:
        print("Queue is empty")
def display():
    print("Queue:", list(queue))

while True:
    print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
