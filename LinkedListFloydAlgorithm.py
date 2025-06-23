class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    
def createLinkedlist(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_entry = None

    for index in range(1, len(values)):
        new_node = ListNode(values[index])
        current.next = new_node
        current = new_node

        if index == pos:
            cycle_entry = new_node

    if pos == 0:
            cycle_entry = head
    if pos != -1:
            current.next = cycle_entry
    return head

def hasCycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
             return True
    
    return False

values = [3, 2, 0, -4]
pos = 1
head = createLinkedlist(values, pos)
print("Cycle detected:" if hasCycle(head) else "No cycle detected.")
