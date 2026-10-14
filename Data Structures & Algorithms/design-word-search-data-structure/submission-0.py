'''
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

    void addWord(word) Adds word to the data structure.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example 1:

Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

Constraints:

    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 2 dots in word for search queries.
    At most 10,000 calls will be made to addWord and search.



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(n) time for each function call and O(t + n) space, where n is the length of the string and t is the total number of nodes created in the Trie.

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()

            current = current.children[w]
        
        current.eow = True

    def search(self, word: str) -> bool:
        def _search(root: TrieNode, k: int) -> bool:
            curr = root
            for i in range(k, len(word)):
                w = word[i]
                if w == '.':
                    for c in curr.children:
                        if _search(curr.children[c], i + 1):
                            return True
                    
                    return False
                if w not in curr.children:
                    return False
                
                curr = curr.children[w]
    
            return curr.eow

        return _search(self.root, 0)
    

        
