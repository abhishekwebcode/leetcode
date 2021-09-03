rep=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
h=dict()
for i in range(ord('a'),ord('z')+1):
    h[i]=rep[i-ord('a')]
del rep
wordToRep= lambda word:"".join(list(map(lambda letter:h[ord(letter)],word)))
wordsToReps = lambda words:list(map(lambda word:wordToRep(word),words))
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(wordsToReps(words)))