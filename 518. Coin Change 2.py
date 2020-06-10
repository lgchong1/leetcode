# 518. Coin Change 2
# by L. Chong
# Time : O(10^5)
# Space: O(amount)

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        #array initializiation
        combos = []
        for _ in range(amount+1):
            combos.append(0)
            
        combos[0]=1
            
        
        for coin in coins:
            for i in range(len(combos)):
                if i >= coin:
                    combos[i] += combos[i-coin]
        #print(combos)

            
        return combos[-1]
