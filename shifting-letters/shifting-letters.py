class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s= [ ord(x)-ord('a') for i,x in enumerate(list(s)) ]
        shifts=shifts[::-1]
        shifts=list(accumulate(shifts))
        shifts=shifts[::-1]
        for i in range(len(shifts)):
            shift=shifts[i]
            s[i]= chr ( ((s[i]+shift)%26)+ord('a') )
        return "".join(s)