class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
         self.left = ListNode(0)
         self.right = ListNode(0)
         self.left.next = self.right
         self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        nextNode = self.left.next
        prevNode = self.left

        prevNode.next = newNode
        nextNode.prev = newNode
        newNode.next = nextNode
        newNode.prev = prevNode


    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        nextNode = self.right
        prevNode = self.right.prev

        prevNode.next = node
        nextNode.prev = node
        node.next = nextNode
        node.prev = prevNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node = ListNode(val)
            nextNode = curr
            prevNode = curr.prev

            prevNode.next = node
            nextNode.prev = node
            node.next = nextNode
            node.prev = prevNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index == 0:
            nextNode = curr.next
            prevNode = curr.prev

            prevNode.next = nextNode
            nextNode.prev = prevNode
# obj.deleteAtIndex(index)