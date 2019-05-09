class Trie():
    
    def __init__(self, value):
        
        self.children = {}
        self.value = value
        self.stopWord = False
        
    @property
    def hasOneChild(self):
        return len(self.children.keys()) == 1
    
    @property 
    def commonPrefix(self):
        
        cur = self
        result = [self.value]
        while cur.hasOneChild and not cur.stopWord:
            result.append(cur.children.keys()[0])
            cur = cur.children[result[-1]]
            
        return result
    
    def addWord(self, word):
        
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie(c)
            cur = cur.children[c]
        
        cur.stopWord = True
        

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        trie = Trie(None)
        for word in strs:
            trie.addWord(word)
        
        return "".join(trie.commonPrefix[1:])
        
