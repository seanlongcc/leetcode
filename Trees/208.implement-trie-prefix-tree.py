#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode():
    def __init__(self):
        self.children = {}
        # example with 'apple'
        # {
        #     'a': {
        #         'p': {
        #             'p': {
        #                 'l': {
        #                     'e': {}
        #                 }
        #             }
        #         }
        #     }
        # }
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # start from the root node
        node = self.root

        # Iterate over each character in the input word
        for char in word:
            # If the current character isn't a child of this node,
            # the word cannot be present in the trie
            if char not in node.children:
                return False
            # Otherwise, move down to the child node for this character
            node = node.children[char]

        # for this problem, the search function is dependent on the insert being done first
        # so it gets set to true in the insert
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # start from the root node
        node = self.root

        # Iterate over each character in the input prefix
        for char in prefix:
            # If the current character isn't a child of this node,
            # the word cannot be present in the trie
            if char not in node.children:
                return False
            # Otherwise, move down to the child node for this character
            node = node.children[char]

        # since it didnt fail, that means it exists
        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
        # @lc code=end
