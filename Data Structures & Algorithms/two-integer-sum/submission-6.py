class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value in nums -> index of value
        prev = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prev:
                return [prev[diff], i]

            prev[num] = i

        return []
