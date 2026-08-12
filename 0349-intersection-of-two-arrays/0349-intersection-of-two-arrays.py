class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        output = []
        # for num1 in nums1:
        #     seen.add(num1)
        
        for num2 in nums2:
            if num2 in seen:
                if num2 not in output:
                    output.append(num2)
        return output
