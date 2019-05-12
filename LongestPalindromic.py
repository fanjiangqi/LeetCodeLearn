#!/usr/bin/env python
#encoding:utf-8
#author: fanjiangqi@gmail.com
#date: 2019-05-12 16:26
#https://leetcode.com/problems/longest-palindromic-substring/
#暴力求解，复杂度n^2

import sys
import ast
import pdb

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = 0
        result = ""
        for i in range(len(s)):
            for j in range(i+1):
                #subLen
                subLen = i - j + 1
                if subLen % 2 != 0:
                    loMid = (i-j) // 2 + j
                    hiMid = (i-j) // 2 + j
                else:
                    loMid = (i-j) // 2 + j
                    hiMid = (i-j) // 2 + j + 1
                if self.isPalindrome(j, loMid, hiMid, s):
                    if subLen > size:
                        size = subLen
                        result = s[j:i+1]
        return result

    def isPalindrome(self, lo, loMid, hiMid, s):
        while lo <= loMid:
            if s[loMid] != s[hiMid]:
                return False
            loMid -= 1
            hiMid += 1
        return True

    
if __name__ == "__main__":
    solution = Solution()
    #s = sys.argv[1]
    #s = "babad"
    s = "cbbd"
    result = solution.longestPalindrome(s)
    print(result)