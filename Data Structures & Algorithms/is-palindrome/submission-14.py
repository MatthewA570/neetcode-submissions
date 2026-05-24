class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalpha() or char.isnumeric()).lower()   
        begin_pointer = 0
        end_pointer = len(s) - 1

        for _ in range(len(s)):
            print(begin_pointer)
            print(len(s))
            print(end_pointer)
            if(s[begin_pointer] == s[end_pointer]):
                begin_pointer +=1
                end_pointer -= 1
                continue
            return False
        return True