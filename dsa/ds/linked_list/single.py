class SinglyLinkedListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    # insertion
    def prepend(self, value):
        # alternatively, return error instead
        if not value:
            return self
        return SinglyLinkedListNode(value, self if self.value else None)

    def append(self, value):
        if not value:
            return self

        curr = self
        while curr.next:
            curr = curr.next
        curr.next = SinglyLinkedListNode(value)
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

    def search():
        pass

    # utilities
    def is_empty(self):
        return bool(self.value)

    def size(self):
        count = 1 if self.value else 0
        curr = self
        while curr.next:
            count += 1
        return count

    def cycles(self):
        pass
