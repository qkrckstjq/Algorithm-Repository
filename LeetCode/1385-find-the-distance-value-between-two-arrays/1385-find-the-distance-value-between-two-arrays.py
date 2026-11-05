class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result = 0
        for num in arr1:
            is_pass = True
            for num2 in arr2:
                if abs(num - num2) <= d:
                    is_pass = False
                    break
            if is_pass:
                result += 1
        return result