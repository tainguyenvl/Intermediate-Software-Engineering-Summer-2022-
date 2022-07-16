'''
Reverse a String

Input: "REVERSE" 
Output: "ESREVER" 

Input: "42 Wallaby Way, Sydney" 
Output: "yendyS ,yaW yballaW 24"

Input: ""
Output: ""
'''

def reverseString(input_str):
  arr = list(input_str)
  start = 0
  end = len(arr) - 1
  while start < end:
    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp
    start = start + 1
    end = end - 1

  return "".join(arr)

print(reverseString("42 Wallaby Way, Sydney"))