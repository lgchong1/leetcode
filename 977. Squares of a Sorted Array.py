# 977. Squares of a Sorted Array
# by L.Chong 4-1-20

# time : O(NlogN) - Python's sort() is based on timsort, which is O(NlogN)
# space: O(N)     - sorts in place, no extra space needed.

class Solution:
	def sortedSquares(self, A:List[int]) -> List[int]:
		for i in range(len(A)):
			A[i] = A[i]*A[i]
		A.sort()
		return A
