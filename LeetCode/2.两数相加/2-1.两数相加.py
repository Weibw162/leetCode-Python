class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode(0)
        current_node = result
        n=0
        while l1 or l2 or n:
            num = (l1.val if l1 else 0)+(l2.val if l2 else 0)+n
            listnode = ListNode(num%10)
            n= num//10
            current_node.next=listnode
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2= l2.next if l2 else None
        return result.next