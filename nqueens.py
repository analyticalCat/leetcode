class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #board 8x8
        #queens move: horizontally, vertically or diagonally.
        #n<=8. 
        if n=1: return 64
        #which column can the first queen be at?

        
    def validCombination(self, n: int):
        for col in range(1,10-n):

            for row in range(1,9):

