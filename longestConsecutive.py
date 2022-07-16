'''
Given an unsorted array of integers, we want to find the length of the longest subsequence such that elements in the subsequence are consecutive integers. The consecutive numbers can be in any order.

Input: [36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42] 
Output: 5 
Note: [36, 35, 33, 34, 32] is the longest subsequence of consecutive elements.

Input: [2] 
Output: 1

Input: [] 
Output: 0

Input: [3, 9, 50, 2, 8, 4, 1]
Output: 4 
Note: [3, 2, 4, 1] is the longest subsequence of consecutive elements.

Input: [1, 5, 29, 4, 3, 2, 1] 
Output: 5 
Note: [1, 5, 4, 3, 2] is the longest subsequence of consecutive elements, 
duplicates don't add to the count.
'''

def longestConsecutive (nums):
  nums = list(set(nums))
  maxLength = curLength = 1
  
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1] - 1:
      curLength += 1
    else:
      curLength = 1
    maxLength = max(maxLength, curLength)
    
  return maxLength

print (longestConsecutive([1, 5, 29, 2, 4, 3, 2, 1] ))
  