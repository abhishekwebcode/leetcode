class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            temp=""
            if not i%3:
                temp+=('Fizz')
            if not i%5:
                temp+=('Buzz')
            if i%3 and i%5:
                temp+=(str(i))
            ans.append(temp)
        return ans