from com.linear.stack_demo import Stack

PROMPT = "Enter an int value (<0 to end): "
class Stack(object):


 myStack = Stack()

 value = int(input(PROMPT))

 while value >= 0:
     myStack.push(value)
     value = int(input(PROMPT))

 while not myStack.isEmpty():
     value = myStack.pop()
     print(value)
