"""
328. Odd Even Linked List
Solved
Medium
Topics
Companies
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = False
        if head == None:
            return head
        if head.next == None:
            return head
        odd = ListNode(val = head.val)
        h_odd = odd
        even = ListNode(val = head.next.val) 
        h_even = even
        curr = head.next.next
        while curr != None:
            if s:
                h_even.next = ListNode(val = curr.val)
                h_even = h_even.next
            else:
                h_odd.next = ListNode(val = curr.val)
                h_odd = h_odd.next
                last = h_odd
            s = not s
            curr = curr.next
        h_odd.next = even
        head = odd
        return head
    
class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head: return None
       
       # odd points to the first node 
       odd = head
       # even points to the second node
       # evenHead will be used at the end to connect odd and even nodes
       evenHead = even = head.next
       
       # This condition makes sure odd can never be None, since the odd node will always be the one before the even node.
       # If even is not None, then odd is not None. (odd before even)
       # If even.next is not None, then after we update odd to the next odd node, it cannot be None. (The next odd node is even.next)
       while even and even.next:
           
           # Connect the current odd node to the next odd node
           odd.next = odd.next.next
           # Move the current odd node to the next odd node
           odd = odd.next
           
           #Same thing for even node
           even.next = even.next.next
           even = even.next
       
       # Connect the last odd node to the start of the even node
       odd.next = evenHead

       # head never changed, so return it
       return head

