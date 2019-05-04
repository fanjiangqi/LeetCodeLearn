#!/usr/bin/env python
#encoding:utf-8
#author: fanjiangqi@gmail.com
#date: 2019-05-04 16:26
#https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

import sys
import ast
import pdb
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        sum = []
        for k in range(len(nums1) + len(nums2)):
            #pdb.set_trace()
            if i == len(nums1) and j < len(nums2):
                sum.append(nums2[j])
                j +=1
            elif j == len(nums2) and i < len(nums1):
                sum.append(nums1[i])
                i +=1
            elif nums1[i] <= nums2[j]:
                sum.append(nums1[i])
                i +=1
            elif nums1[i] > nums2[j]:
                sum.append(nums2[j])
                j +=1
        k = len(sum)
        if k % 2 == 0:
            return (sum[k/2-1] + sum[k/2]) * 1.0/2
        else:
            return sum[k/2]

if __name__== "__main__":
    #print 'fanjiangqi'
    solution = Solution()
    nums1 = ast.literal_eval(sys.argv[1])
    nums2 = ast.literal_eval(sys.argv[2])
    #print len(nums1)
    #print nums2
    #print range(len(nums1) + len(nums2))
    result = solution.findMedianSortedArrays(nums1,nums2)
    print result