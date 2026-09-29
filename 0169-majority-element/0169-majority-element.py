class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, values in hashmap.items():
            if values > (len(nums)/2):
                return key
