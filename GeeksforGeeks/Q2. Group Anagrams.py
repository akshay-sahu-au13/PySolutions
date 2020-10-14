### https://leetcode.com/problems/group-anagrams/submissions/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        Anagrams = {}
        
        for i in strs:
            
            key = "".join(sorted(i))
            
            if key not in Anagrams:
                
                Anagrams[key] = [i]
                
            else:
                
                Anagrams[key].append(i)
                
        return (list(Anagrams.values()))