class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        count = 1
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left+=1 
                nums[left] = nums[right]
                count+=1 
        return count

        

        

