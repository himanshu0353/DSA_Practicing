class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for sttr in patterns:
            if sttr in word:
                count += 1
        return count