class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_l = 0

        indexs = {}

        for pts in range(0, len(s)):
            if(s[pts] in indexs.keys()):
                start = max([start, indexs[s[pts]]])
            max_l = max([max_l, pts - start + 1])
            indexs[s[pts]] = pts + 1

        return max_l
