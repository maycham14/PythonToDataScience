class LinkedList:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new_node = self._Node(data)
        if self._is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, key):
        if self._is_empty():
            return False
        elif self.head == self.tail:
            if key == self.head.data:
                return True
            else:
                return False
        else:
            current = self.head
            while current is not None:
                if current.data == key:
                    return True
                else:
                    current = current.next
            return False

    def _is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def display_nodes(self):
        current = self.head
        while current is not None:
            print(f"Node: {current.data}")
            current = current.next  #

    def delete_node(self, key):
        if self._is_empty():
            return False
        elif self.head == self.tail:
            if key == self.head.data:
                self.head = self.tail = None
                return True
            else:
                return False
        elif key == self.head.data:
            self.head = self.head.next
            return True
        else:
            current = self.head
            while current.next is not None:
                if key == current.next.data:
                    current.next = current.next.next
                    return True
                else:
                    current = current.next
            return False


lists = LinkedList()
lists.add_head(113)
lists.add_head(12)
lists.add_head(13)
lists.add_head(15)
lists.add_head(14)
lists.add_head(15)
print(lists.find(113))
print(lists.delete_node(15))
print(lists.delete_node(15))
lists.display_nodes()
