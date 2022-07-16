'''
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

def isPalindromeRecursive(st, s, e):
    if (s == e):
        return True

    if (st[s] != st[e]):
        return False
                
    if (s < e + 1):
        return isPalindromeRecursive(st, s + 1, e - 1);
 
    return True
 
def isPalindrome(st):
    n = len(st)
    if (n == 0):
        return True
     
    return isPalindromeRecursive(st, 0, n - 1);


print(isPalindrome('geadaeg'))