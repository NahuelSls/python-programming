'''
Stack Data Structure
'''
# Creating a Stack class with its important or main methods
class Stack():
    # initializing items with an empty list
    def __init__(self):
        self.items = []

    # creating the push method to add items to our list using append
    def push(self, item):
        self.items.append(item)

    # pop method to eliminate the last item added to our list
    def pop(self):
        return self.items.pop()

    # empty method that returns True or False if the list its empty or not
    def is_empty(self):
        return self.items == []

    # peek method that return the last item value
    def peek(self):
        if not self.is_empty(): # but the if conditions only works if the list is not empty
            return self.items[-1]

    # this method returns the value of the list with their current items
    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')

print('Your stack:', myStack.get_stack())
print('\nThe last element added to your stack:', myStack.peek())
print('\nIs your stack empty?', myStack.is_empty())

myStack.pop()
print('\nYour new stack after popping the last element:', myStack.get_stack())
