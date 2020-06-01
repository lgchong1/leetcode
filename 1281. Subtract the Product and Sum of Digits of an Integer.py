# 1281. Subtract the Product and Sum of Digits of an Integer
# by L. Chong
# Time : O(1)
# Space: O(1)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumV = 0
        
        while n>0:
            #print(n)
            flt = n/10
            n = n//10
            #print("\t",flt)
            #print("\t",n)
            val = round((flt - n) * 10)
            #print("\t",val)
            prod *= val
            sumV += val
            #print("\t",prod)
            #print("\t",sumV)

        return prod-sumV
