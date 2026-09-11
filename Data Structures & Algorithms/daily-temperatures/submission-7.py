class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #start from right
        res = [0] * len(temperatures) # it is 0 if not found
        stack = [] #(index and temperature) 
        #keep the temperature still waiting to get a warmer date the buttom has to be the not matched warmest temp
        
        for i, t in enumerate(temperatures): 
            while stack and t > stack[-1][1]: 
                stackInd, stackT = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append((i,t))
        return res

