'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true

Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true

Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false

Constraints:

    1 <= s.length <= 200
    1 <= wordDict.length <= 100
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.

'''
'NON OPTIMAL'
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a full word into the Trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the exact word exists in the Trie."""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns True if any word in the Trie starts with the given prefix."""
        return self._find_node(prefix) is not None

    def delete(self, word: str) -> bool:
        """Removes a word from the Trie. Returns True if the word was found and deleted."""
        def _delete_helper(current: TrieNode, index: int) -> bool:
            if index == len(word):
                if not current.is_end_of_word:
                    return False  # Word does not exist
                current.is_end_of_word = False
                return len(current.children) == 0  # Prune node if it has no children

            char = word[index]
            if char not in current.children:
                return False

            should_delete_child = _delete_helper(current.children[char], index + 1)

            if should_delete_child:
                del current.children[char]
                return not current.is_end_of_word and len(current.children) == 0

            return False

        was_present = self.search(word)
        if was_present:
            _delete_helper(self.root, 0)
        return was_present

    def _find_node(self, prefix: str) -> TrieNode | None:
        """Helper method to traverse down to the end of a prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for w in wordDict:
            trie.insert(w)

        stack = [0]
        checked = set()
        while stack:
            k = stack.pop()
            
            if k in checked:
                continue

            checked.add(k)
            # print(f'{checked=}, {k=}')

            if k == len(s):
                return True
            
            for i in range(k, len(s) + 1):
                # print(f'{i=}, {s[k:i]=}')
                if trie.search(s[k:i]) == True:
                    stack.append(i)
                    # print(f'{stack=}, {s[k:i]=}')
                    
        return False


        