

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        in_cnt = 1
        de_cnt = 1

        for i in range(1, len(nums)):
            prev_num = nums[i - 1]
            cur_num = nums[i]
            
            if prev_num < cur_num:
                in_cnt += 1
                de_cnt = 1
            elif prev_num > cur_num:
                de_cnt += 1
                in_cnt = 1
            else:
                in_cnt = 1
                de_cnt = 1
            
            answer = max(answer, in_cnt, de_cnt)
            
        return answer