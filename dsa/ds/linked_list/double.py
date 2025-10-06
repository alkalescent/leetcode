class DoublyLinkedListNode:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # insertion
    def prepend(self, value):
        # alternatively, return error instead
        if not value:
            return self
        node = DoublyLinkedListNode(value, None, self if self.value else None)
        self.prev = node
        return node

    def append(self, value):
        if not value:
            return self

    # value and position
    def insert():
        pass

    # deletion
    # take position
    def pop():
        pass

    def del_val():
        pass

    # traversal and search
    def traverse():
        pass

    def search(self, value):
        pass
    # utilities

    def size(self):
        count = 1 if self.value else 0
        curr = self
        while curr.next:
            count += 1
        return count

    def cycles(self):
        pass
