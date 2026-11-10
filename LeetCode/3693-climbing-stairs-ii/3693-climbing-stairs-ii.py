# 한번에 최대 3칸까지 점프가능
# 점프 했을때 소모되는 cost = costs[i] + (dst - src)^2
# 
#

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [math.inf  for _ in range(len(costs) + 1)]
        for i in range(min(3, len(costs))):
            dp[i + 1] = costs[i] + pow(i + 1, 2)
        dp[0] = 0
        
        # print(dp)
        

        for i in range(len(costs)):
            src = costs[i]
            prev_cost = dp[i + 1]

            if i + 1 < len(costs):
                cur_cost = costs[i + 1] + 1
                dp[i + 2] = min(dp[i + 2], prev_cost + cur_cost)
            
            if i + 2 < len(costs):
                cur_cost = costs[i + 2] + 4
                dp[i + 3] = min(dp[i + 3], prev_cost + cur_cost)
            
            if i + 3 < len(costs):
                cur_cost = costs[i + 3] + 9
                dp[i + 4] = min(dp[i + 4], prev_cost + cur_cost)

            # if i + 2 < len(dp):
            #     cost2 = src + pow(i + 2 - i, 2)
            #     dp[i + 2] = min(dp[i + 2], cost2)

            # if i + 3 < len(dp):
            #     cost3 = src + pow(i + 3 - i, 2)            
            #     dp[i + 3] = min(dp[i + 3], cost3)

            # print(dp)
        return dp[len(costs)]