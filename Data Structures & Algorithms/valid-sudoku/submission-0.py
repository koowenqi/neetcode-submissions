class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = {}
        for i in range(len(board)):
            for x in range(len(board[i])):
                box_id = (i//3, x//3)
                if box_id not in square:
                    square[box_id] = set()
                if board[i][x] in square[box_id] and board[i][x] != ".":
                    return False
                square[box_id].add(board[i][x])
        
        for i in range(len(board)):
            hashset1 = set()
            for x in board[i]:
                if x in hashset1 and x != ".":
                    return False
                hashset1.add(x)
                
        dict1 = {}
        for i in range(9):
            for x in range(9):
                if x not in dict1:
                    dict1[x] = set()
                if board[i][x] in dict1[x] and board[i][x] != ".":
                    return False
                dict1[x].add(board[i][x])
        return True