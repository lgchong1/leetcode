# 412. Fizz Buzz
# by L.Chong, 4/26/20

# Time : O(N)
# Space: O(N)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        j = 1
        
        while j < n + 1:
            if j % 5 == 0 and j % 3 == 0:
                output.append('FizzBuzz')
            elif j % 3 == 0:
                output.append('Fizz')
            elif j % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(j))
            j+=1
        
        return output
