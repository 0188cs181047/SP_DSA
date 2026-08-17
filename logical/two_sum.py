"""
Two Sum — Definition

Two Sum is a common array problem where, given an array of integers and a target value, 
we need to find two different elements whose sum is equal to the target.


Example
    Input:
    nums = [2, 7, 11, 15]
    target = 9

    2 + 7 = 9
"""

class Solution:
    def twoSum(self, array, target):
        see = {}

        for i, val in enumerate(array):
            if (target-val) in see:
                return (see[target-val], i)
            else:
                see[val] = i


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(nums, target=target)
    print(res)