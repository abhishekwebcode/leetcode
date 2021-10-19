class Solution:
    def originalDigits(self, s: str) -> str:
        rep=[
            'zero','one','two','three','four',
            'five','six','seven','eight','nine'
        ]
        m={
            'w':2,
            'u':4,
            'z':0,
            'x':6,
            'g':8,
        }
        left={
            'h':3,
            'o':1,
            'f':5,
            's':7,
            'i':9
        }
        s=Counter(s)
        numbers=[]
        for uniqChar in m:
            number = m[uniqChar]
            freq=s[uniqChar]
            numbers.extend([number]*freq)
            word = rep[number]
            for char in word:
                s[char]-=freq
        for uniqChar in left:
            number = left[uniqChar]
            freq=s[uniqChar]
            numbers.extend([number]*freq)
            word = rep[number]
            for char in word:
                s[char]-=freq
        return "".join([str(x) for x in sorted(numbers)])