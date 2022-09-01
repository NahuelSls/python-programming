'''
Singly linked lists
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# starting with append method in the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # this method will add new nodes to an empty linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()


