class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            IP = IP.split('.')
            if len(IP)==4 and all(x.isdigit() and x==str(int(x)) and 0<=int(x)<=255 for x in IP):
                return 'IPv4'
        elif ':' in IP:
            IP = IP.split(':')
            if len(IP)==8 and all( 1<=len(x)<=4  for x in IP ):
                for part in IP:
                    try:
                        int(part,base=16)
                    except:
                        return 'Neither'
                return 'IPv6'
        return 'Neither'