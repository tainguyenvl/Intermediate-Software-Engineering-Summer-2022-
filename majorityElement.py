'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(nums):
  dic = {}
  for i in range(len(nums)):
    if nums[i] in dic:
      dic[nums[i]] += 1
    else:
      dic[nums[i]] = 1

  for k,v in dic.items():
    if v >= len(nums)/2:
      return k

print(majorityElement([2,2,1,1,1,2,2]))