class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result =0
        result_str = []
        for i in s:
            if i in result_str: result_str =result_str[result_str.index(i)+1:]
            result_str.append(i)
            result=max(len(result_str),result)
        return result

if __name__=='__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("aab"))
