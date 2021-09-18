class Node:
    def __init__(self):
        self.dict=defaultdict(Node)
        self.exists=False
        self.came=False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie=Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr=self.trie
        curr.came=True
        for c in word:
            curr=curr.dict[c]
            curr.came=True
        curr.exists=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr=self.trie
        for c in word:
            curr=curr.dict[c]
        return curr.exists
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr=self.trie
        for c in prefix:
            curr=curr.dict[c]
        return curr.came


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)