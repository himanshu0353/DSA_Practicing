class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        hashmap = {}
        
        for right in range(len(s)):
    
            while s[right] in hashmap:
                del hashmap[s[left]]
                left+=1
            hashmap[s[right]] = 1
            ans = max(ans, right-left+1)
        return ans