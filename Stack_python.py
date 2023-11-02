def create_stack():
  st= []
  return st

# Pushing elements into stack
def push(st,x):
  st.append(x)
  print("pushed element",x)

# Checking size of stack
def size(st):
  return len(st)

# Checking if stack is empty or not
def is_empty(st):
  if size(st) == 0:
    return True
  else:
    return False

# Removing element from stack
def pop(st):
  if is_empty(st) == True :
    return "Pop does not exist"
  else:
    st.pop()
    return "Poped out last element"

# Last element
def peek(st):
  if is_empty(st) == True:
    return -1
  else:
    return st[-1]

stack = create_stack()
push(stack,7)
print(peek(stack))
pop(stack)
print(is_empty(stack))
