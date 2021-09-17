class Solution:
    def reorderSpaces(self, text: str) -> str:
        o=text
        spaces=text.count(r" ")
        text=[x for x in text.split(" ") if x.strip()]
        print(text)
        if len(text)==1:
            print('len 1')
            return text[0]+(" "*spaces)
        bw=int(spaces/(len(text)-1))
        extra=int(spaces-(bw*(len(text)-1)))
        return (" "*bw).join(text)+(" "*extra)