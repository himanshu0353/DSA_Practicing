class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = []
        left = 0
        right = len(numbers) - 1

        while left < right :
            if numbers[left] + numbers[right] == target:
                index.append(left+1)
                index.append(right+1)
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
                
        return index
                