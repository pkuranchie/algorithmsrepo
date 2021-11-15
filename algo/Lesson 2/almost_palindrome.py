# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z and it's not a palindrome.


# radkar
# redarop
#

# O(n) n = len(s)
def is_almost_palindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i + 1]
        if t == t[::-1]:
            return True

    return s == s[::-1] # return False

str_pose = 'radkar'
str_neg = 'redarop'

print(is_almost_palindrome(str_pose)) # True
print(is_almost_palindrome((str_neg))) # False