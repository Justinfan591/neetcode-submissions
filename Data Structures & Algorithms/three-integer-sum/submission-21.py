class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #pair negative with positives and other ones would be 3 zeros. Wait, it could be 1 zero and  no zeros
        res = []
        sort = sorted(nums)
        def twosum(start,target, sort):
            ans = []
            l = start
            r = len(nums) - 1
            anchor = target
            target = -target
            while r>l:
                if sort[r] + sort[l] > target: 
                    r-=1
                elif sort[r] + sort[l] < target: 
                    l+=1
                elif sort[r] + sort[l] == target:
                    ans.append([sort[r],sort[l],anchor])
                    l += 1
                    while l < r and sort[l] == sort[l - 1]:
                        l += 1
            return ans


        i = 0
        while i < len(sort) - 2:
            if i > 0 and sort[i] == sort[i - 1]:
                i += 1
                continue
            res.extend(twosum(i + 1, sort[i], sort))
            i += 1
        
        return res


            
