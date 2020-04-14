# 767. Reorganize String
# by L. Chong, 4/13/20

# space: O(N)
# time : O(NlogN)


class Solution:
    def reorganizeString(self, S: str) -> str:
        cDict = {}
        
        for c in S:
            if c not in cDict:
                cDict[c] = 1
            else:
                cDict[c] += 1
                
        #print('total dictionary:', cDict)
        
        #in the event that one character is more than half of all characters
        
        for k,v in cDict.items():
            if v >= len(S)/2+1:
                return ""
            
        output = []
       
        maxK = None
        maxV = -1
        while cDict:
            for k,v in cDict.items():
                #print(k,v)
                
                if v > maxV:
                    if not output:
                        maxV = v
                        maxK = k
                    elif k != output[-1]:
                        maxV = v
                        maxK = k
                                    
            print('max k,v: ',maxK,maxV)
            
            output.append(maxK)
            
            #print(output)
            
            cDict[maxK]-=1
            if cDict[maxK] == 0:
                del cDict[maxK]
                
            maxK = None
            maxV = -1
            
        return "".join(output)
                    
