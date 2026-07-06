class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # stores the target - num 
        # value is index of that num
        suffixes = {}

        for i, num in enumerate(nums):
            if num in suffixes:
                return [suffixes[num], i]
            else:
                suffixes[target - num] = i


        