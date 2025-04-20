class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=s.replace(" ","").lower()
        t=t.replace(" ","").lower()

        return Counter(s)==Counter(t)