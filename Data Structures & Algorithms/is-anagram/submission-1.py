class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        # if(hash(s) == hash(t)):
        #     return True
        # return False
    
