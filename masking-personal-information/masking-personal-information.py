SEP="".join(['+', '-', '(', ')', ' '])
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            [username,domain]=s.split('@')
            mid="*"*5
            return (username[0]+mid+username[-1]+"@"+domain).lower()
        else:
            for c in ['+', '-', '(', ')', ' ']:
                s="".join(s.split(c))
            countryLen=len(s)-10
            local=s[-10:]
            if not countryLen:
                return "***-***-"+local[-4:]
            if countryLen==1:
                return "+*-***-***-"+local[-4:]
            if countryLen==2:
                return "+**-***-***-"+local[-4:]
            return "+***-***-***-"+local[-4:]