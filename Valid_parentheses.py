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

# Valid Parentheses
def valid_parentheses(s):
  st = []
  for i in range(len(s)):
    if s[i] == '(' or s[i] == '{' or s[i] == '[':
      st.append(s[i])
    elif s[i] == ')' :
      if len(st) == 0 or st[-1] != '(':
        return False
      else:
        st.pop()
    elif s[i] == ']' :
      if len(st) == 0 or st[-1] != '[':
        return False
      else:
        st.pop()
    elif s[i] == '}' :
      if len(st) == 0 or st[-1] != '{':
        return False
      else:
        st.pop()

  if len(st) == 0:
    return True
  else:
    return False



print(valid_parentheses("[{(})]"))

print(valid_parentheses("[{()}]"))
