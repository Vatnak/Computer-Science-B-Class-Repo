def push(stack, value):
    stack.append(value)
    return stack

def pop(stack):
    if not stack:
        return None
    else:
        return stack.pop(-1)

def is_empty(stack):
    if not stack:
        return True
    else: 
        return False
    
stack = []
print(push(stack, 5))
print(push(stack, 10))
print(push(stack, 15))
print(pop(stack))
print(is_empty(stack))
print(push(stack, 20))

#Check and Explain 

# Empty stack
empty = []
print(pop(empty))        # None
print(is_empty(empty))   # True

# One-element stack
one = [7]
print(pop(one))          # 7
print(is_empty(one))     # True (after the pop)

# Why does 15 leave first? Stacks are LIFO — pop(-1) removes from the same end push adds to, so the most recently pushed value (15) comes off first.
# return vs print: print only displays a value; return hands it back to the caller so it can be stored or reused.