class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.endOfWord = True

    def countPrefix(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        return node.count - 1 if node.endOfWord else node.count


def findCompletePrefixes(names, query):
    trie = Trie()
    for name in names:
        trie.insert(name)

    result = []
    for q in query:
        result.append(trie.countPrefix(q))

    return result



