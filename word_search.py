class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(word, i, j, board):
                    return True
        return False

    def dfs(self, word, i, j, board):
        
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or board[i][j] != word[0] or i > len(board) or j > len(board[0]):
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        if board[i][j] == word[0]:
            res = self.dfs(word[1:], i - 1, j, board) or self.dfs(word[1:], i + 1, j, board) or self.dfs(word[1:], i,
                                                                                                         j - 1,
                                                                                                         board) or \
                  self.dfs(word[1:], i, j + 1, board)

        return res
