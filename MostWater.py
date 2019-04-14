#!/usr/bin/env python
#encoding:utf-8
#author: fanjiangqi@gmail.com
#date: 2019-04-14 23:50

import sys
import ast

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        maxWater = 0
        while lo < hi:
            maxWater = max(maxWater, min(height[lo],height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return maxWater

if __name__== "__main__":
    #print 'fanjiangqi'
    solution = Solution()
    height = ast.literal_eval(sys.argv[1])
    result = solution.maxArea(height)
    print result