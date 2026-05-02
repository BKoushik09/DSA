'''undo_stack = []
redo_stack = []
undo_stack.append('india')
undo_stack.append('Brazil')
undo_stack.append('China')
print("current stack:", undo_stack)
if len(undo_stack)>0:
    action = undo_stack.pop()
    undo_stack.append(action)
    print("undo:", action)
print("current stack:", undo_stack)
if len(redo_stack)>0:
    action = redo_stack.pop()
    redo_stack.append(action)
    print("redo: ", action)
print("redo stack:", redo_stack)'''


#applications of stack for menu-driven operations
'''undo_stack = []
redo_stack = []
while True:
    print("\n1. Perform Action")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        action = input("Enter choice:")
        undo_stack.append(action)
        redo_stack.clear()
        print("Action Performed:", action)
    elif choice == 2:
        if len(undo_stack) == 0:
            print("undo stack is empty")
        else:
            action = undo_stack.pop()
            redo_stack.append(action)
            print("Undo:", action)
    elif choice == 3:
        if len(redo_stack) == 0:
            print("redo stack is empty")
        else:
            action = redo_stack.pop()
            undo_stack.append(action)
            print("Redo:", action)
    elif action == 4:
        print("Undo stack:", undo_stack)
        print("Redo stack:", redo_stack)
    elif action == 5:
        break
    else:
        print("Invalid choice")'''


'''undo_stack = []
redo_stack = []
filename = 'sample.txt'
try:
    with open(filename, 'r') as f:
        text = f.read()
except:
    text = ''
while True:
    print("\n1. Perform Action")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        newtext = input("enter text:")
        undo_stack.append(text)
        text += newtext
        redo_stack.clear()
        with open(filename, 'w') as f:
            f.write(text)
        print("written in file")
    elif choice == 2:
        if len(undo_stack) == 0:
            print("Nothing to perform")
        else:
            redo_stack.append(text)
            text = undo_stack.pop()
            with open(filename, 'w') as f:
                f.write(text)
            print("Undo performed")
    elif choice == 3:
        if len(redo_stack) == 0:
            print("Nothing to perform redo")
        else:
            undo_stack.append(text)
            text = redo_stack.pop()
            with open(filename, 'w') as f:
                f.write(text)
            print("Redo performed")
    elif choice == 4:
        with open(filename, 'r') as f:
            print("file content:", f.read())
    elif choice == 5:
        break
    else:
        print("Invalid choice")'''

#check for balanced paranthesis
'''s = input("enter the expression:")
stack = []
valid = True
for ch in s:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]':
        if len(stack) == 0:
            valid = False
            break
        top = stack.pop()
        if (ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '['):
            valid = False
            break
if len(stack) != 0:
    valid = False
if valid:
    print("Balanced")
else:
    print("not balanced")'''

#balancing the expression
s = input("enter the expression:")
stack = []
result = ''
for ch in s:
    if ch == '(':
        stack.append(ch)
        result += ch
    elif ch == ')':
        if len(stack) > 0:
            stack.pop()
            result += ch
        else:
            result = '(' + result + ')'
while len(stack) > 0:
    result += ')'
    stack.pop()
print("balanced expression:", result)


s = input("enter infix expression:")
stack = []
result = ''
priority = {'+': 1, '-': 1, '*': 2, '/': 2}
for ch in s:
    if ch.isalnum():
        result += ch
    elif ch 


s = input("enter the expression:")
stack = []
for ch in s:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a+b)
        elif ch == '-':
            stack.append(a-b)
        elif ch == '*':
            stack.append(a*b)
        elif ch == '/':
            stack.append(a/b)
print("result:", stack.pop())
    