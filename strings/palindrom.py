""" 6.5 Check if string is palindrome.

A man, a plan, a canal, Panama
Able wa I, ere I saw Elba
Ray a Ray - not

Move pointers from both ends skipping non-alphanum characters

Why not
return all(s[i] == s[~i] for i in range(len(s) // 2))

Maybe because of skipping non-alphanum characters
"""


def is_palindrome(s):
    i, j = 0, len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1

    return True
