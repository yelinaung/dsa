"""
from https://albertauyeung.github.io/2020/06/15/python-trie.html/
"""

from dataclasses import dataclass, field


@dataclass
class TrieNode:
    char: str
    is_end: bool = False
    counter: int = 0
    children: dict = field(default_factory=dict)


@dataclass
class Trie:
    root = TrieNode("")  # base empty node

    def __repr__(self):
        return f"{self.root}"

    def insert(self, word: str):
        node = self.root
        # loop through each char in the word
        # check whether the children contain the char
        # else create a new child for the current Node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # create a new node in the trie
                # if a char is not found
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # mark the end of a word
        node.is_end = True

        # increment the counter to indicate that
        # we see this word once more
        node.counter += 1

    def search(self, word):
        """
        given an input x, search all words stored in the trie
        with that prefix, sort the words by the number of times
        they have been inserted
        """
        print(f"searching for {word}")
        self.output = []
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs_hepler(node, word[:-1])
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def dfs_hepler(self, node, prefix):
        """
        depth first traversal of the trie"
        node    : the node to start with
        prefix  : the current prefix, for tracing a word while
                  traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs_hepler(child, prefix + node.char)


t = Trie()
t.insert("was")
t.insert("wat")
t.insert("war")
t.insert("what")
t.insert("which")
t.insert("where")
print(t.search("wa"))
print(t.search("wh"))
print(t.search("w"))
