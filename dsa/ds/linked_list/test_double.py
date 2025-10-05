from double import DoublyLinkedListNode


class TestDoublyLinkedList:
    def test_init(self):
        node = DoublyLinkedListNode()
        assert not node.value
        assert not node.next
        assert not node.prev

        node = DoublyLinkedListNode(1)
        assert node.value == 1
        assert not node.next
        assert not node.prev

        node_b = DoublyLinkedListNode(4)
        node_a = DoublyLinkedListNode(1, None, node_b)
        node_b.prev = node_a

        node = node_a
        assert node.value == 1
        assert node.next
        assert node.next.value == 4
        assert not node.next.next
        assert node.next.prev.value == 1

    def test_prepend(self):
        node = DoublyLinkedListNode(1).prepend(None)
        assert node.value == 1
        assert not node.next
        assert not node.prev

        node = DoublyLinkedListNode().prepend(1)
        assert node.value == 1
        assert not node.next
        assert not node.prev

        node = DoublyLinkedListNode("old_first").prepend("new_first")
        assert node.value == "new_first"
        assert node.next.value == "old_first"
        assert not node.next.next
        assert not node.prev
        assert node.next.prev.value == "new_first"
