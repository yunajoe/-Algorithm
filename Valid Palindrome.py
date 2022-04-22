import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # converting all uppercase letters into lowercase letters
                     # removing all non-alphanumeric characters,  숫자랑 문자를 제외한 나머지것들을 다지웡!
        new_s = "".join(al for al in s if al.isalnum())
        if new_s[::] == new_s[::-1]:
            return True
        return False