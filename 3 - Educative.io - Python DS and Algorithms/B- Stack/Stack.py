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

    # empty method that returns True or False if the list is empty or not
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
print("\nBefore adding some elements:")
print('Is your stack empty?', myStack.is_empty()) # True

# we push some elememts to our stack
myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')

print('\nYour stack:', myStack.get_stack()) # ['A', 'B', 'C', 'D']
print('The last element added to your stack:', myStack.peek()) # D
print('After adding items, is your stack empty?', myStack.is_empty()) # False

myStack.pop()
print('\nYour new stack after popping the last element:', myStack.get_stack()) # ['A', 'B', 'C']


