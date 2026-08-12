class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False

        for ss in s:
            count[ss] = count.get(ss, 0)+ 1
        
        for tt in t:
            if tt not in count:
                return False
            
            count[tt] -= 1

            if count[tt] < 0:
                return False
        return True
