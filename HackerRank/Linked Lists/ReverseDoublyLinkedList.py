# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    if head is None:
        return head
    else:
        last =  head
        current = head
        iterator = head
        while iterator is not None:
            current = iterator
            iterator = iterator.next

            temp = current
            current.next = current.prev
            current.prev = temp.next

        return current
