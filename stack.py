# Implementation of stack using Linked list

# Implement the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next.data

# Implement the Stack class
class Stack:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        stack = []
        for node in self:
            stack.append(node.data)
        # stack.append("None")
        return " --> ".join(stack)

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def whatever_you_want(self):
        # TODO Whatever you feel like
        pass

    def pop(self):
        if not self.head:
            raise Exception("Cannot pop from an empty stack")
        else:
            self.head = self.head.next

# Main function, instantiate an empty stack and push in some values
def main():
    stack = Stack()
    stack.push("Cédric")
    stack.push("Aidan")
    stack.push("Daenerys")
    stack.push("Biden")
    stack.push("Harris")
    stack.push("Elon Musk")

    print("Full stack: {}".format(stack))

    stack.pop()
    stack.pop()

    print("Stack after two pops: {}".format(stack))


if __name__ == "__main__":
    main()
