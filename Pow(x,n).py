'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

'''

def myPow(x, n):
  if n == 0:
    return 1
  
  elif n == 1:
    return x
  
  elif n == -1:
    return 1/x

  lower = myPow(x, n//2)
  if n % 2 == 0: return lower*lower
  if n % 2 == 1: return lower*lower*x

print(myPow(2,5))