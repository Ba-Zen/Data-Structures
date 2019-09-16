from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if not self.storage:
            return
        else:
            return self.storage.pop()

    def len(self):
        return len(self.storage)
