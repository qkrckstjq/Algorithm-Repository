class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        avg = sorted(nums)[len(nums) // 2]
        result = 0
        for num in nums:
            result += abs(avg - num)
        return result