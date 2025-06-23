# 🧠 Problem: Linked List Cycle Detection
# Given the head of a singly linked list, determine if the linked list has a cycle in it.
# A cycle occurs when a node's next pointer points to a previous node in the list,
# forming an infinite loop.

# 💡 Approach:
# We'll use Floyd’s Cycle Detection Algorithm (Tortoise and Hare technique),
# which uses two pointers moving at different speeds. If there's a cycle,
# they will eventually meet. This approach uses O(1) space and O(n) time.

# ------------------------------------------------------

# 🔧 Node definition for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       # stores the value of the node
        self.next = next     # reference to the next node (initially None)

# 🔧 Helper function to create a linked list from a list of values
# If pos != -1, creates a cycle at the node located at index `pos`
def createLinkedlist(values, pos):
    if not values:
        return None  # empty list, return None

    head = ListNode(values[0])  # create the head node
    current = head              # pointer to track current node while building list
    cycle_entry = None          # will store reference to node where cycle starts

    for index in range(1, len(values)):
        new_node = ListNode(values[index])  # create a new node
        current.next = new_node             # link it to the list
        current = new_node                  # move the pointer

        if index == pos:
            cycle_entry = new_node  # mark the cycle entry point

    if pos == 0:
        cycle_entry = head  # if cycle is at head

    if pos != -1:
        current.next = cycle_entry  # create the cycle

    return head

# 🚀 Function to detect if the linked list contains a cycle
def hasCycle(head) -> bool:
    slow = fast = head  # initialize both pointers at head

    while fast and fast.next:
        slow = slow.next           # move slow pointer by 1 step
        fast = fast.next.next      # move fast pointer by 2 steps

        if slow == fast:
            return True  # cycle detected

    return False  # if loop ends, no cycle is present

# 🧪 Example usage
values = [3, 2, 0, -4]  # input list
pos = 1  # index at which the last node will point to create a cycle (0-based)
head = createLinkedlist(values, pos)  # create the linked list with a cycle

# ✅ Check for cycle and print result
print("Cycle detected:" if hasCycle(head) else "No cycle detected.")
