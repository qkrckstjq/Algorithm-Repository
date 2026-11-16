class Solution:
    def digitSum(self, s: str, k: int) -> str:
        arr = list(s)
        step = ""
        while len("".join(arr)) > k:
            temp = []
            cnt = 0
            temp_num = 0
            for i, c in enumerate(arr):
                # print(temp_num, cnt)
                if cnt < k:
                    temp_num += int(c)
                    cnt += 1
                else:
                    temp.append(str(temp_num))
                    temp_num = int(c)
                    cnt = 1
                if i == len(arr) - 1:
                    temp.append(str(temp_num))
                
            # print(temp)
            step = "".join(temp)
            arr = list(step)
        # print(arr)
        return "".join(arr)
