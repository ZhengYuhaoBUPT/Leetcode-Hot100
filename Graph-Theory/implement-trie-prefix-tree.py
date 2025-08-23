class Node:

    def __init__(self):
        self.son = {}
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """

        cur = self.root
        # put the word in the tree
        for c in word:
            # if there is no son before
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def find(self, word):
        cur = self.root
        # search
        for c in word:
            # if not in cur, then there is no this word
            if c not in cur.son:
                return 0
            # if there is c, continue to search
            cur = cur.son[c]
        # if end is true, there is this word in
        # else only have the startswith
        return 2 if cur.end else 1

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        # use find to get whether match
        return self.find(word) == 2

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        # find if have prefix
        # if not zero, there is prefix
        return self.find(prefix) != 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
