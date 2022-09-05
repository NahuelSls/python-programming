'''
Singly linked lists
'''
# First of all we create the Node class that is going to be useful for the other class and methods
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

    # this method print our linked list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # a method to delete a node
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

    # with this method we can delete any node at position X
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # with this method we can calculate the lenght of the linked list - iterative
    def len_iterative(self):
        count = 0
        len_ite = self.head

        while len_ite:
            count += 1
            len_ite = len_ite.next
        return count

    # with this method we can calculate the length of the linked list - recursive
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    # mehtod that help us to swap nodes
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next




llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("G")

llist.prepend("E")

llist.insert_after_node(llist.head.next, "F")

llist.delete_node("C")

llist.delete_node_at_pos(1)

print("\nIterative - Length:", llist.len_iterative())
print("Recursive - Length:", llist.len_recursive(llist.head))

print("\nOriginal list:")
llist.print_list()

print("\nSwapping nodes F and G:")
llist.swap_nodes("F", "G")
llist.print_list()



