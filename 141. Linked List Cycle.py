# Code created 3/30/20
# by Lawrence Chong
# Based on solution algorithm in leetcode.



class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		if head is None or head.next is None:
			return False
		turt = head
		rab  = head.next

		while turt != rab:
			if rab is None or rab.next is None:
				return False
			turt = turt.next
			rab  = rab.next.next
		return True
