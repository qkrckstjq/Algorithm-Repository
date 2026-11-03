class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        result = 0
        for num in nums:
            result += (max_num - num)
        return result