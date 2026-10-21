class Solution:
    def threeSum(self, nums: list[int]): 
        if len(nums) < 3: 
            return []
        order = sorted(nums)
        ans = []
        i = 0
        while i < len(nums) - 2: 
            j = i + 1
            k = len(nums) - 1

            while j < k: 
                total = order[i] + order[j] + order[k]
                if total < 0: 
                    while j<k and order[j] == order[j+ 1]: 
                        j+= 1
                    j += 1
                elif total > 0:
                    while j<k and order[k] == order[k -1]:
                        k-=1 
                    k-=1
                else: #found
                    ans.append([order[i], order[j], order[k]])
                    while j<k and order[j] == order[j + 1]: 
                        j += 1
                    while j<k and order[k] == order[k-1]: 
                        k -=1
                    j += 1
                    k -= 1

            while i< len(order) - 2 and order[i] == order[i + 1]: 
                i += 1
            i += 1
            
        return ans
