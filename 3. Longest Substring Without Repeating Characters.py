# 3. Longest Substring Without Repeating Characters
# by L.Chong

# Brute force Impl:
#	Time : O(N^2)
#	Space: O(N)

# Sliding Window Impl:
#	Time : O(N)
#	Space: O(N)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
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
        '''
        
        i, cnt = 0,0
        
        substr = []
        
        while i < len(s):
            #print("i": ",i, "    s[i]:",s[i],"   substr:",substr)
            if s[i] not in substr:
                substr.append(s[i])
                i+=1
                cnt = max(len(substr), cnt)
            else:
                while substr and s[i] != substr.pop(0):
                    pass
                    #print("   ", substr)
                
        return cnt
