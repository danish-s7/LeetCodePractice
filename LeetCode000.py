class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[comp] = i
        
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target) == [0, 1])
