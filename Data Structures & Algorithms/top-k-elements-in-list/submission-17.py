class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #edge cases: k = 0, return []
        if k == 0: 
            return []
        #run through the entire things first
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        # we just need to find the most frequent once, so we can sort the dictionary
        sorted_dic = sorted(dic.items(), key = lambda p: p[1], reverse = True)  #this would return a List
        ans = []
        for i in range(k): 
            ans.append(sorted_dic[i][0])

        return ans
            


