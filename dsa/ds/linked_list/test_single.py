from single import SinglyLinkedListNode


class TestSinglyLinkedList:
    def test_init(self):
        node = SinglyLinkedListNode()
        assert not node.value
        assert not node.next

        node = SinglyLinkedListNode(1)
        assert node.value == 1
        assert not node.next

        node = SinglyLinkedListNode(1, SinglyLinkedListNode(4))
        assert node.value == 1
        assert node.next
        assert node.next.value == 4
        assert not node.next.next

    def test_prepend(self):
        node = SinglyLinkedListNode(1).prepend(None)
        assert node.value == 1
        assert not node.next

        node = SinglyLinkedListNode().prepend(1)
        assert node.value == 1
        assert not node.next

        node = SinglyLinkedListNode("old_first").prepend("new_first")
        assert node.value == "new_first"
        assert node.next.value == "old_first"
        assert not node.next.next

    def test_append(self):
        node = SinglyLinkedListNode(1).append(None)
        assert node.value == 1
        assert not node.next

        node = SinglyLinkedListNode().append(1)
        assert node.value == 1
        assert not node.next

        node = SinglyLinkedListNode("old_last").append("new_last")
        assert node.value == "old_last"
        assert node.next.value == "new_last"
        assert not node.next.next

    def test_del_val(self):
        node = SinglyLinkedListNode()
        assert not node.del_val(None)

        node = SinglyLinkedListNode(1)
        assert node.del_val(2) == node

        node = SinglyLinkedListNode(1)
        assert not node.del_val(1)

        node = SinglyLinkedListNode(1, SinglyLinkedListNode(4))
        assert node.del_val(1).traverse() == [4]

        node = SinglyLinkedListNode(1, SinglyLinkedListNode(4))
        assert node.del_val(4).traverse() == [1]

        node = SinglyLinkedListNode(
            1, SinglyLinkedListNode(4, SinglyLinkedListNode(2)))
        assert node.del_val(1).traverse() == [4, 2]
        node = SinglyLinkedListNode(
            1, SinglyLinkedListNode(4, SinglyLinkedListNode(2)))
        assert node.del_val(4).traverse() == [1, 2]
        node = SinglyLinkedListNode(
            1, SinglyLinkedListNode(4, SinglyLinkedListNode(2)))
        assert node.del_val(2).traverse() == [1, 4]

    def test_traverse(self):
        node = SinglyLinkedListNode()
        assert node.traverse() == []

        node = SinglyLinkedListNode(1)
        assert node.traverse() == [1]

        node = SinglyLinkedListNode(1, SinglyLinkedListNode(4))
        assert node.traverse() == [1, 4]

        node = SinglyLinkedListNode(
            1, SinglyLinkedListNode(4, SinglyLinkedListNode(2)))
        assert node.traverse() == [1, 4, 2]

    def test_search(self):
        node = SinglyLinkedListNode()
        assert node.search(1) == -1

        node = SinglyLinkedListNode(1)
        assert node.search(1) == 0
        assert node.search(2) == -1

        node = SinglyLinkedListNode(1, SinglyLinkedListNode(4))
        assert node.search(1) == 0
        assert node.search(4) == 1
        assert node.search(2) == -1

        node = SinglyLinkedListNode(
            1, SinglyLinkedListNode(4, SinglyLinkedListNode(2)))
        assert node.search(1) == 0
        assert node.search(4) == 1
        assert node.search(2) == 2

    def test_size(self):
        node = SinglyLinkedListNode()
        assert node.size() == 0

        node = SinglyLinkedListNode("old_first")
        assert node.size() == 1

        node = node.prepend("new_first")
        assert node.size() == 2

        node = node.append("new_last")
        assert node.size() == 3
