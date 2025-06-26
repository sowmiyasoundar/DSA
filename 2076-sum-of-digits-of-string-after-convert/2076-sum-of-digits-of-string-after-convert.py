class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=''
        for c in s:
            pos=(ord(c)-ord('a')+1)
            num+=str(pos)
        while k>0:
            sum=0
            for d in num:
                sum+=int(d)
            num=str(sum)
            k-=1
        return int(num)