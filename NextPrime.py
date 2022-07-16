'''
Next Prime
Given a number, return the next smallest prime number

Input: 5
Output: 7

Input: 1
Output: 2

EDGE CASE:
Input: -10
Output: 2
The smallest prime number is 2, so any input less than 2 should return 2

'''
import math 

def is_Prime(n):
  if n < 2:
    return False

  if n < 4:
    return True

  for i in range (2, int(math.sqrt(n))+1):
    if n % i  == 0:
      return False
  return True

def next_Prime(n):
  if n <= 1:
    return 2

  n += 1
  while True:
    if is_Prime(n):
      return n
    n += 1

print(next_Prime(5))