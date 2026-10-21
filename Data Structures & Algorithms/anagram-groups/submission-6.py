class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dictionary of dictionaries, wait we can sort
        if len(strs) == 0: 
            return []
        
        dic = {} 
        for string in strs: 
            ordered = "".join(sorted(string))
            if ordered in dic: 
                dic[ordered].append(string)
            else: 
                dic[ordered] = [string]
        return list(dic.values())