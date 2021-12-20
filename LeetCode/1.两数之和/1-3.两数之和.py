class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = dict()
        for index,value in enumerate(nums):
            if target-value in record and record[target-value]!=index:
                return [index,record[target-value]]
            else:
                record[value]=index


if __name__=='__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))
    print(solution.twoSum([3,3],6))
