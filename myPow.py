"""Iterative approach"""

"""Accepted for first test case but throws memory error"""

#Time complexity - O(n) where n is the power
#Space complexity - O(1)


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #Edge case
        if n == 0:
            return 1.0
        if n == 1:
            return x
        res = 1.0
        #handling the negative powers
        if n < 0:
            x = 1.0/x
            n = -n
            
        for i in range(n):
            res = res * x
        return res