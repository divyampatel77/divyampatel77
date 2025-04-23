# Program 7 - Stack
stack = []
def push():
    val = input("Enter value to push: ")
    stack.append(val)
def pop():
    if stack:
        print("Popped:", stack.pop())
    else:
        print("Stack is empty")
def display():
    print("Stack:", stack)

while True:
    print("\n1.Push 2.Pop 3.Display 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
