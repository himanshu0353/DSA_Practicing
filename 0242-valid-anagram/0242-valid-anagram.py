class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for si in s:
            hashmap[si] = hashmap.get(si, 0) + 1

        for ti in t:
            if ti not in hashmap:
                return False
            
            hashmap[ti] -= 1

            if hashmap[ti] < 0:
                return False
            
        return True