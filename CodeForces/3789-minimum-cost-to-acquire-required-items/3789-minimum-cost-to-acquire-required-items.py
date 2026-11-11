# 2중 배열 dp?
# cost1 = 5, cost2 = 4, costboth = 15, need1 = 2, need2 = 3
# cost1 * 2 + cost2 * 3 = 22
# need1 = y
# need2 = x

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        s_n = min(need1, need2)

        rem1 = min(s_n * cost1 + s_n * cost2, s_n * costBoth)

        e_n = max(need1, need2) - s_n

        r_c = cost1 if max(need1, need2) == need1 else cost2

        rem2 = min(e_n * r_c, e_n * costBoth)

        return (rem1 + rem2)


        # longer_need = max(need1, need2) + 1
        # dp = [[math.inf for _ in range(longer_need)] for _ in range(longer_need)]
        # if need1 == 0 and need2 == 0:
        #     return 0
        # if need1 == 0:
        #     return min(need2 * cost2, costBoth * need2)
        # if need2 == 0:
        #     return min(need1 * cost1, costBoth * need1)

        # dp[0][0] = 0
        # # for i in range(longer_need):
        # #     dp[0][i] = 0
        # #     dp[i][0] = 0
        
        # # print(dp)

        # for i in range(longer_need):
        #     for j in range(longer_need):
        #         if i + 1 < longer_need:
        #             dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cost1)

        #         if j + 1 < longer_need:
        #             dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + cost2)

        #         if i + 1 < longer_need and j + 1 < longer_need:
        #             dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + costBoth)
        #             dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + costBoth)
        #             dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + costBoth)
                
        #         # print(dp)
        
        # # for row in dp:
        # #     print(row, "\n")
        # return dp[need1][need2]


# 1,000,000,000