class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # print(round(1 / 2))

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1)
        left_have = (len(nums1) + len(nums2) + 1) // 2
        i = (left + right) // 2
        j = left_have - i

        # print(i, j)

        a_left = -math.inf if i - 1 < 0 else nums1[i - 1]
        a_right = math.inf if i >= len(nums1) else nums1[i]

        b_left = -math.inf if j - 1 < 0 else nums2[j - 1]
        b_right = math.inf if j >= len(nums2) else nums2[j]

        # print(a_left, a_right)
        # print(b_left, b_right)

        while a_left > b_right or b_left > a_right:
            # print(a_left, a_right)
            # print(b_left, b_right)


            if a_left > b_right:
                right = i - 1 # 왼쪽이 비교적 크기 때문에 왼쪽으로 이동
            elif b_left > a_right:
                left = i + 1 # 왼쪽이 비교적 작기 때문에 오른쪽으로 이동

            i = (left + right) // 2
            j = left_have - i

            a_left = -math.inf if i - 1 < 0 else nums1[i - 1]
            a_right = math.inf if i >= len(nums1) else nums1[i]

            b_left = -math.inf if j - 1 < 0 else nums2[j - 1]
            b_right = math.inf if j >= len(nums2) else nums2[j]

        # print(a_left, a_right)
        # print(b_left, b_right)

        return max(a_left, b_left) if (len(nums1) + len(nums2)) % 2 != 0 else (max(a_left, b_left) + min(a_right, b_right)) / 2