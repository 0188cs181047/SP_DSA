class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printLL(self):
        if self.head is None:
            return

        current = self.head
        while current:
            print(current.data, end="->")

            current = current.next

            

if __name__ == "__main__":
    s_ll = SingleLL()
    s_ll.insert_at_beginning(1)
    s_ll.insert_at_beginning(11)
    s_ll.insert_at_beginning(111)
    s_ll.insert_at_beginning(1111)

    s_ll.printLL()

