class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

class Solution(object):
    def __init__(self):
        self.result = []

    def findWords(self, board, words):
        # Build the trie
        root = self.buildTrie(words)
        
        # Traverse each cell in the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root)
        
        return self.result

    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
            node.word = word
        return root

    def dfs(self, board, i, j, node):
        # Boundary check and if character is in children
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return

        char = board[i][j]
        next_node = node.children[char]
        
        # If we found a word, add it to results and mark it as found
        if next_node.is_word:
            self.result.append(next_node.word)
            next_node.is_word = False  # Avoid duplicate words
        
        # Mark the cell as visited
        board[i][j] = '#'
        
        # Explore all four directions
        self.dfs(board, i + 1, j, next_node)
        self.dfs(board, i - 1, j, next_node)
        self.dfs(board, i, j + 1, next_node)
        self.dfs(board, i, j - 1, next_node)
        
        # Restore the cell's original value for backtracking
        board[i][j] = char

        # Optimization: remove leaf nodes
        if not next_node.children:
            node.children.pop(char)
