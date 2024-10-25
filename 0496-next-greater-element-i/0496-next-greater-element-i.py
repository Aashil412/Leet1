class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_element = {}

        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            
            next_greater_element[num] = stack[-1] if stack else -1
            stack.append(num)
        
        results = []

        for num in nums1:
            results.append(next_greater_element[num])
        return results
            
            
        