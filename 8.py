class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        inti=1
        i=0
        res=''
        if len(s)>0:
            if s[0]=="-":
                inti=-1
                s=s[1:]
            elif s[0]=='+':
                s=s[1:]
            while i<len(s):
                if not s[i].isdigit():
                    break
                else:
                    res+=s[i]
                i+=1
            if res=='':
                return 0
            else:
                res=inti*int(res)
                if res>2147483647:
                    res=2147483647
                elif res<-2147483648:
                    res=-2147483648
                return res
        else:
            return 0     
