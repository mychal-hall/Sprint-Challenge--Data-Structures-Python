class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

# Iterative solution to reverse the list

# Set previous as None, current as head and next as the next node of current

# Iterate through the linked list until current is None (this is the loop’s exit condition)

# During each iteration, set the next node of current to previous

# Then, set previous as current, current as next and next as its next node (this is the loop’s iteration process)

# Once the current becomes None, set the head pointer to the previous node

    def reverse_list(self):
        # TO BE COMPLETED
        prev = None
        current = self.head
        # Iteration
        while current:
            temp = current.next_node
            current.set_next(prev)
            # Moving to the next node
            prev = current
            current = prev
            current = temp
            # Initializing head
        self.head = prev
