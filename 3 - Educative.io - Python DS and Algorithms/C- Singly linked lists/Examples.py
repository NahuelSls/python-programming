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

    # method that add a new node before the head of the linked list
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # method that add a new node after an existing one
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def delete_node(self, key):
        cur_node = self.head

        # case of deleting head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # case of deleting node other than the head
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("E")

llist.insert_after_node(llist.head.next, "F")

llist.delete_node("C")

llist.print_list()




