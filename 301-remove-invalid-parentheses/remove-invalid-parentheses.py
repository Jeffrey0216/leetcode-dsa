class Solution:
    def removeInvalidParentheses(self,s):
        def valid(s):
            c=0
            for x in s:
                if x=='(':
                    c+=1
                elif x==')':
                    c-=1
                    if c<0:
                        return False
            return c==0

        q=[s]
        v={s}

        while q:
            r=[x for x in q if valid(x)]
            if r:
                return r
            nq=[]
            for x in q:
                for i in range(len(x)):
                    if x[i] in '()':
                        y=x[:i]+x[i+1:]
                        if y not in v:
                            v.add(y)
                            nq.append(y)
            q=nq