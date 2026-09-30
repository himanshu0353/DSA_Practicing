class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0 
        low = 0
        high = len(height) - 1

        while low<high:
            if height[low] <= height[high]:
                current_area = height[low] * (high-low)
                low+=1
                area = max(area,current_area)
            elif height[high] <= height[low]:
                current_area = height[high] * (high-low)
                high -= 1
                area = max(area, current_area)
        return area
            
    