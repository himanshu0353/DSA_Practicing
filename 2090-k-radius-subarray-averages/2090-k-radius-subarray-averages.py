class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_size = 2*k +1

        if window_size > len(nums):
            return [-1]*len(nums)

        ans = [-1]*len(nums)

        window_sum = 0
        for i in range(window_size):
            window_sum += nums[i]

        ans[k] = window_sum // window_size

        for i in range(window_size, len(nums)):
            window_sum = window_sum + nums[i] - nums[i-window_size]

            center = i - k

            ans[center] = window_sum // window_size

        return ans


    

