class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map dic first
        dic = {}
        for num in nums: 
            if num in dic: 
                dic[num] += 1
            else: dic[num] = 1
        pairs = sorted(dic.items(), key = lambda p:p[1], reverse = True)
        res = []
        for i in range(k):
            res.append(pairs[i][0])
        return res
