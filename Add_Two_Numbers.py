# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper to convert a Python list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper to print linked list as a Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Solution class
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# 🧪 Example test
l1 = list_to_linkedlist([2, 4, 3])  # represents 342
l2 = list_to_linkedlist([5, 6, 4])  # represents 465

sol = Solution()
result_node = sol.addTwoNumbers(l1, l2)
print("Result as list:", linkedlist_to_list(result_node))  # Output: [7, 0, 8] (342 + 465 = 807)
