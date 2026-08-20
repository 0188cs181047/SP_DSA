class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLL:
    def __init__(self):
        self.head = None


    def insert_at_end(self, data):
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def printLL(self):
        if self.head is None:
            return None

        current = self.head

        while current:
            print(current.data, end="->")

            current = current.next 

    

if __name__ == "__main__":
    s = SingleLL()
    s.insert_at_end(1)
    s.insert_at_end(22)
    s.insert_at_end(333)
    s.insert_at_end(44444)

    s.printLL()