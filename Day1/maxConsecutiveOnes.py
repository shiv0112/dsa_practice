"""485. Max Consecutive Ones
Easy
5.4K
449
Companies
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1."""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        c=0
        flag=0
        for num in nums:
            if flag==1 and num==1:
                flag=1
                c+=1
            elif flag==0 and num==1:
                flag=1
                c=1
            else:
                flag=0
                c=0
            m = c if c>m else m
        return(m)