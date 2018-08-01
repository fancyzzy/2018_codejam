#!/usr/bin/env python3

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for k in t_dict.keys():
            if k not in s_dict.keys():
                return k
            else:
                if s_dict[k] != t_dict[k]:
                    return k


if __name__ == '__main__':
    s = 'abcd'
    t = 'abcde'
    sol = Solution()
    res = sol.findTheDifference(s,t) 
    print(res)