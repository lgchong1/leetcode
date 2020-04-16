# 1221. Split a String in Balanced Strings
# by L. Chong, 04/16/20

# Stack Impl
#   Time : O(N)
#   Space: O(N)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        stack = []
        for elem in s:
            print(elem)
            
            if not stack:
                stack.append(elem)
            elif stack[-1] != elem:
                stack.pop()
            else:
                stack.append(elem)
            if not stack:
                cnt +=1
                
            print(stack)
                
        return cnt
