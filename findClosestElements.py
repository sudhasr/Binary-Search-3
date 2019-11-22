"""Binary search approach"""
#Accepted on leetcode
#Time complexity - O(max(logN,k))
#Space omplexity - O(1) or O(k)


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = []
        NOE = k
        target = x
        low = 0
        high = len(arr)-NOE-1
        #1) Find the starting point
        while low <= high:
            mid = low + (high - low)/2
            if abs(arr[mid] - target) > abs(arr[mid+NOE]-target):
                low = mid+1
            else:
                high = mid - 1
        #2) Add elements to the list with starting point
        for i in range(NOE):
            res.append(arr[low + i])
        return res