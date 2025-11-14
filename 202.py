class Solution(object):
    def isHappy(self, n,repeat=None):
        if repeat is None:
            repeat=[]
        if n==1:
            return True 
        if n in repeat:
            return False
        repeat.append(n)       
        res=[]
        new_n=0
        if n%10==0 and n!=0:
            res=[int(d) for d in str(n)]
        else:
            while n>0:
                rem=n%10
                n=n//10
                res.append(rem)
        for i in res:
            new_n+=i*i
        return self.isHappy(new_n,repeat)
