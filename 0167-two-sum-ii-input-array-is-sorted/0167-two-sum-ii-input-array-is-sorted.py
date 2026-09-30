class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        for i in range(len(numbers)):
            if numbers[low] + numbers[high] == target:
                return [low+1,high+1]
            elif numbers[low] + numbers[high] > target:
                high -=1
            else :
                low+= 1