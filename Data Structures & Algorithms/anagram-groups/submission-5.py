class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dictionary of dictionaries, wait we can sort
        dic = {}
        ans = []
        
        for string in strs: 
            temp = "".join(sorted(string))
            if temp in dic: 
                dic[temp].append(string)
            else: 
                dic[temp] = [string]
        
        for value in dic.values():
            ans.append(value)
        return ans