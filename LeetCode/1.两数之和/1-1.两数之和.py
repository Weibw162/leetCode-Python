class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for f_index in range(len(nums)-1):
            for s_index in range(f_index+1,len(nums)):
                if nums[f_index]+nums[s_index]==target:
                    return [f_index,s_index]

if __name__=='__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))
    print(solution.twoSum([3,3],6))
