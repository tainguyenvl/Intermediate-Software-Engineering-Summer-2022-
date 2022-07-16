'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def lengthOfLongestSubstring( s: str) -> int:
  seen = {}
  l = 0
  output = 0
  for r in range(len(s)):
      if s[r] not in seen:
          output = max(output,r-l+1)
      else:
          if seen[s[r]] < l:
              output = max(output,r-l+1)
          else:
              l = seen[s[r]] + 1
      seen[s[r]] = r
  return output

print(lengthOfLongestSubstring('abcabbb'))