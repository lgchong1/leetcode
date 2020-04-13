# 345. Reverse Vowels of a String.py
# Brute force Impl
# Time : O(N)
# Space: O(N)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u',\
                  'A','E','I','O','U']
        myStack = []
        for char in s:
            if char in vowels:
                myStack.append(char)
        print(myStack)
        final = []
        for i in range(len(s)):
            if s[i] in vowels:
                final.append(myStack.pop())
            else:
                final.append(s[i])
                
        print(final)
        
        return ''.join(final)
