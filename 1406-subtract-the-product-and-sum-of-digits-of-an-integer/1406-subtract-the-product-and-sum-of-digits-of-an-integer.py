class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=list(map(int,str(n)))
        p=1
        s=0
        for d in x:
            p*=d
            s+=d

        return (p-s)