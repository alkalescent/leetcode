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
