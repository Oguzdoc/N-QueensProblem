from typing import List

# Exhaustive Search Implementation
class ExhaustiveSearch:
        
    def __init__(self,sizeOfBlock) -> None:
        """
        Initialize the ExhaustiveSearch class with a given board size.
        """
        self.CreateNBoard(sizeOfBlock)
        pass
    
    def CreateNBoard(self,sizeOfBlock):
        """
        Create an N x N chessboard and initialize supporting data structures.
        - sizeOfBlock: Size of the chessboard (N).
        """
        self.sizeofBlock = sizeOfBlock
        self.colums = [0 for i in range(sizeOfBlock)]
        self.diagonals =[0 for i in range(2*sizeOfBlock)]
        self.antiDiagonals =[0 for i in range(2*sizeOfBlock)]
        self.chessBoard =[['x' for i in range(sizeOfBlock)] for j in range(sizeOfBlock)]
        self.solutions: List[str] = []

    def DisplayBoard(self,board):
        """
        Display the given chessboard solution.
        - board: List of strings representing the chessboard state.
        """        
        for solution in board:
            print(f'{" ".join(solution)}')
                
    def DepthFirstSearch(self,row: int = 0) -> bool:
        """
        Perform a depth-first search to solve the N-Queens problem.
        - row: Current row being processed (default is 0).
        Returns True if a solution is found, otherwise False.
        """        
        if(row == self.sizeofBlock):
            # Base case: all rows are processed; save the solution
            for i in range(self.sizeofBlock):
                self.solutions.append("".join(self.chessBoard[i]))
            self.DisplayBoard(self.solutions)                    
            return True
        
        for col in range(self.sizeofBlock):
             # Skip columns and diagonals already under attack
            if self.colums[col] or self.diagonals[row+col] or self.antiDiagonals[self.sizeofBlock - row + col]:
                continue
            # Place a queen and mark the column/diagonals as occupied
            self.chessBoard[row][col] = 'Q'
            self.colums[col] = self.diagonals[row+col] = self.antiDiagonals[self.sizeofBlock - row + col] = 1
            # Recur for the next row
            if self.DepthFirstSearch(row +1):
                return True
            # Backtrack: remove the queen and unmark the column/diagonals
            self.chessBoard[row][col] = 'x'
            self.colums[col] = self.diagonals[row+col] = self.antiDiagonals[self.sizeofBlock - row + col] = 0
        
        return False
    
