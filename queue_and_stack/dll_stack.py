from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if not self.storage:
            return None
        else:
            return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.storage)
print(s.pop())
