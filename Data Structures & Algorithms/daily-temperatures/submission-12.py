class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures) 

        #stack stores the ones still need to find a warmer day. Once found, we subtract to get the days. Hence we keep the index

        for i in range(len(temperatures)): 
            if len(stack) == 0: 
                stack.append((i,temperatures[i]))
            
            else: 
                current = temperatures[i]
                while stack: 
                    if stack[-1][1] < current: 
                        temp = stack.pop()
                        ans[temp[0]] = i  - temp[0]
                    else: 
                        stack.append((i,current))
                        break # I think this break while loop
                else: stack.append((i,current))
        return ans
                

