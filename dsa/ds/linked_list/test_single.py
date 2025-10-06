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

    def test_size(self):
        node = SinglyLinkedListNode()
        assert node.size() == 0

        node = SinglyLinkedListNode("old_first")
        assert node.size() == 1

        node = node.prepend("new_first")
        assert node.size() == 2

        node = node.append("new_last")
        assert node.size() == 3
