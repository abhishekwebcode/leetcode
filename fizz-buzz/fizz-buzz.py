class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(0,n):
            ind = i+1
            if ind%3==0 and ind%5==0:
                ans.append('FizzBuzz')
            elif ind%3==0:
                ans.append('Fizz')
            elif ind%5==0:
                ans.append('Buzz')
            else:
                ans.append(str(ind))
        return ans