"""Determine if string is a mirror palindrome.

121 = True
926 = True
373 = False
160991 = True
"""


def is_mirror_palindrome(s):
  d = {'0': '0', '1': '1', '6': '9', '9': '6'}

  for i in range(len(s) // 2):
     first = s[i]
     last = s[~i]
     first_pair = d.get(first, None)
     if last != first_pair:
       return False

  return True
