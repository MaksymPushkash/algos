'''
Trie(Prefix Tree)/Autocomplete
Префіксне дерево


Він посимвольно розбиває нашу послідовність, 
для кожного символа створює ноду, а до дитини він переходить по наступному символу.


Пошук винонується за O(n), вставка за O(n) також.
 Бо кожен показник на дитину зберігається в хеш мапі ноди.
'''


'''
208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., 
was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string 
word that has the prefix prefix, and false otherwise.

'''

class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.terminal = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.terminal


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# ==========================================================================================


'''
1268. Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after 
each character of searchWord is typed. Suggested products should have common prefix with
 searchWord. If there are more than three products with a common prefix return the three 
 lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].


'''
from typing import List

# class Node...
    
# class Trie...

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    root = Trie()

    for word in products:
        root.insert(word)
    
    result = []

    for i in range(len(searchWord)):
        found = root.search(searchWord[:i+1])

        if found:
            result.append(sorted(found)[:3])
        else:
            result.append([])

    return result

