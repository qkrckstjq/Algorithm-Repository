class Solution:
    def processStr(self, s: str) -> str:
        result = []

        words = list(s)

        for c in words:
            if c == "*":
                if result:
                    result.pop()
            elif c == "#":
                # if result:
                #     for cp in result.copy():
                #         result.append(cp)
                # result = result[::-1]
                result += result
            elif c == "%":
                result = result[::-1]
            else:
                result.append(c)
            
            # print(result)

        return "".join(result)