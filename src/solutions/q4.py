from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        lo, hi = -1, n1 - 1
        # 用 i j 分割，如果是偶数个，希望左边数量是一半，如果是奇数个，希望左边数量多一个
        # 约定 i+0.5 是分割线，所以 i/j 可能取值 -1
        while lo < hi:
            i = (lo + hi + 1) // 2
            j = (n1 + n2 + 1) // 2 - (i + 1) - 1
            # print('i = ', i); print('j = ', j)
            if j < n2 - 1 and nums1[i] > nums2[j+1]:
                hi = i - 1
            elif i < n1 - 1 and nums1[i+1] < nums2[j]:
                lo = i + 1
            else:
                lo = hi = i
        i = lo
        j = (n1 + n2 + 1) // 2 - (i + 1) - 1
        # print(nums1, nums2, i, j)
        ls = []
        rs = []
        if n1 > 0 and i >= 0: ls.append(nums1[i])
        if n1 > 0 and i + 1 < n1: rs.append(nums1[i+1])
        if j >= 0: ls.append(nums2[j])
        if j + 1 < n2: rs.append(nums2[j+1])
        if (n1 + n2) % 2 == 0:
            return (max(ls) + min(rs)) / 2
        else:
            return max(ls)
