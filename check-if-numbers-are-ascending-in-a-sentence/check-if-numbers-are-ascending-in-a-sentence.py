class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = None
        for word in s.split(' '):
            try:
                i = int(word)
                if prev is not None and not (i>prev):
                    return False
                prev = i
            except:
                pass
        return True