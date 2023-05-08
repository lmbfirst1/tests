"""
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        char = set()
        p = 0
        while(p<len(nums)):
            if(nums[p] in char):
                nums.remove(nums[p])
            else:
                char.add(nums[p])
                p = p+1
                
        #print(nums)
        return len(char)