"""
https://leetcode.com/problems/duplicate-zeros/editorial/
The problem demands the array to be modified in-place. If in-place was not a constraint 
we might have just copied the elements from a source array to a destination array.
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        a= []
        for i in range(len(arr)):
            if arr[i]==0:
                a.append(i)
        k =0
        for i in range(len(a)):
            arr.insert(a[i]+k,0)
            k+=1
        m = len(arr)
        for i in range(m-n):
            arr.pop()
        return arr
        