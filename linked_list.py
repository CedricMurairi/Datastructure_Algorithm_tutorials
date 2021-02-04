# stack and queue implementation using Linked list

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        lst = []
        for node in self:
            lst.append(node.data)
        return " --> ".join(lst)

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
        # add at the head
        # node.next = self.head
        # self.head = node
        # add at the tail
            current = None
            for nd in self:
                current = nd
            current.next = node
                

    def remove(self, data):
        if not self.head:
            raise Exception("Cannot remove from empty list")

        if self.head.data == data:
            self.head = None
            return
        
        previous = None
        for nd in self:
            if nd.data == data:
                previous.next = nd.next
                break
            previous = nd

# Stack class

# Queue class

# Main
def main():
    students = LinkedList()

    print("Empty list: {}".format(students))

    students.add("Cédric")
    students.add("Elon Musk")
    students.add("Bezoss")
    students.add("DJ Trump")

    print("Full list: {}".format(students))

    students.remove("Bezoss")

    print("List after one delete: {}".format(students))

if __name__ == "__main__":
    main()
