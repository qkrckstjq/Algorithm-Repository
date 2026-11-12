# 합치고 재정렬?

# 2 2 4 4 | 2 2 2 4 4
# 2 2 2 2 2 4 4 4 4

# 1 2 | 3 4
# 1 2 3 4
# 5 / 2 = 2.5

# 이진 탐색

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merge_arr = nums1 + nums2
        merge_arr.sort() # n log n
        # print(merge_arr)
        # print(len(merge_arr) / 2)

        if len(merge_arr) % 2 == 0:
            m_l = merge_arr[len(merge_arr) // 2 - 1]
            m_r = merge_arr[len(merge_arr) // 2]
            print(m_l, m_r)
            return (m_l + m_r) / 2
        else:
            return merge_arr[len(merge_arr) // 2]
        # return 0

