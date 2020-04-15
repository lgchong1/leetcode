# 3. Longest Substring Without Repeating Characters
# by L. Chong, 4/15/20

# Time : O(N^2)
# Space: O(N)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        final = 0
       
        for i in range(len(s)):
            chars = []
            j = i
            count = 0
            if final > len(s)-j:
                #print('final:',final,"  j:",j,"  len(s)-j:",len(s)-j)
                #print('early return')
                return final
            while j < len(s) and s[j] not in chars:
                count+=1
                chars.append(s[j])
                #print(chars)
                j+=1
            if count > final:
                final = count           
            

            
        print('late return')
        return final
