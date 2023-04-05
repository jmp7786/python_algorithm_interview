# https://leetcode.com/problems/palindrome-pairs/
import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def insert(self, index: int, word: str) -> None:
        node = self.root

        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_ids.append(index)
            node = node.children[char]

        node.word_id = index

    def search(self, index: int, word: str) -> List[List[int]]:
        node = self.root
        result = []
        while word:
            if node.word_id >= 0 and self.is_palindrome(word):
                result.append([index, node.word_id])
            if word[0] not in node.children:
                return result

            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and index != node.word_id:
            result.append([index, node.word_id])

        for i in node.palindrome_ids:
            result.append([index, i])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        result = []
        for i, word in enumerate(words):
            trie.insert(i, word)

        for i, word in enumerate(words):
            result.extend(trie.search(i, word))

        return result