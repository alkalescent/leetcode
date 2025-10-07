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
    def pop(self, index):
        head = self
        iter_idx = 0
        curr = self
        # if index == iter_idx and curr.next:
        #     curr.next = curr.next.next
        if index == 0:
            return self.next
        while curr.next:
            iter_idx += 1
            if index == iter_idx:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    def del_val(self, value):
        # also (if not self OR if not self.value OR ...)
        if self.value == value:
            return self.next

        head = self
        curr = self
        while curr and curr.next:
            # look at curr.next.value
            if curr.next.value == value:
                curr.next = curr.next.next
            curr = curr.next

        return head

    # traversal and search
    def traverse(self):
        nodes = []
        curr = self
        if curr.value:
            nodes.append(curr.value)
        while curr.next:
            nodes.append(curr.next.value)
            curr = curr.next
        return nodes

    def search(self, value):
        # returns index of value
        curr = self
        found_idx = -1
        iter_idx = 0
        while curr.next:
            if curr.value == value:
                found_idx = iter_idx
            curr = curr.next
            iter_idx += 1
        if curr.value == value:
            found_idx = iter_idx
        return found_idx

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
