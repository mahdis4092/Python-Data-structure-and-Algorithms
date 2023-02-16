'''

def create_stack():
    stack=[]
    return stack
def IsEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item +" Item push on the stack")
def pop(stack):
    if len(stack)==0 :
        return str(-1)
    else:
       return stack.pop()
def peek(stack):
    if len(stack)==0:
        return str(-1)
    else:
        return stack[len(stack)-1]





stack=create_stack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
print(pop(stack) + "pop from stack")
print(peek(stack) + "peek item from stack")
'''