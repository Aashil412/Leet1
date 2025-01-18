class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        N, M = len(nums1), len(nums2)
        results = []
        while i < N and j < M:
            if nums1[i] == nums2[j]:
                results.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return list(set(results))
        