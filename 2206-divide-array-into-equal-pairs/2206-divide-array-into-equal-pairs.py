class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_dic = {}
        for num in nums:
            if num not in count_dic:
                count_dic[num] = 1
            else:
                count_dic[num] += 1
        for num in count_dic:
            if count_dic[num] % 2 != 0:
                return False
        return True
