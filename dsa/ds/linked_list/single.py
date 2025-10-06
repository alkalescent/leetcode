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
        node = SinglyLinkedListNode(value)
        if self.value:
            curr.next = SinglyLinkedListNode(value)
            return self
        return node

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
        # returns index of value
        curr = self
        found_idx = -1
        iter_idx = 0
        while curr.next:
            # if
            curr = curr.next
            iter_idx += 1
        # TODO: come back to this

    # utilities
    def size(self):
        count = 1 if self.value else 0
        curr = self
        while curr.next:
            count += 1
            curr = curr.next
        return count

    def cycles(self):
        pass
