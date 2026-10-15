class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def print_ll(self):
        if self.head:
            current = self.head
            while current:
                print(current.data, end="->")
                current = current.next

            print(None)

    def get_middle(self):
        slow = self.head 
        fast = self.head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        return slow



ll = LL()
ll.insert(1)
ll.insert(11)
ll.insert(111)
ll.insert(1111)
ll.insert(11111)

ll.print_ll()
print(ll.get_middle().data)