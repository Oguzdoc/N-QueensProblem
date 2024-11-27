from typing import List

class ExhaustiveSearch:
        
    def __init__(self, sizeOfBlock) -> None:
        """
        Initialize the ExhaustiveSearch class with a given board size.
        """
        self.CreateNBoard(sizeOfBlock)
    
    def CreateNBoard(self, sizeOfBlock):
        """
        Create an N x N chessboard and initialize supporting data structures.
        """
        self.sizeofBlock = sizeOfBlock
        self.columns = [0] * sizeOfBlock
        self.diagonals = [0] * (2 * sizeOfBlock)
        self.antiDiagonals = [0] * (2 * sizeOfBlock)
        self.chessBoard = [['x'] * sizeOfBlock for _ in range(sizeOfBlock)]
        self.solutions: List[List[str]] = []

    def DisplayBoard(self, board):
        """
        Display the given chessboard solution.
        - board: List of strings representing the chessboard state.
        """
        for solution in board:
            print(f'{" ".join(solution)}')
        print("\n")  # Separate multiple solutions
                
    def DepthFirstSearch(self, row: int = 0) -> bool:
        """
        Perform a depth-first search to solve the N-Queens problem.
        - row: Current row being processed (default is 0).
        Returns True if a solution is found, otherwise False.
        """
        if row == self.sizeofBlock:
            # Base case: all rows are processed; save the solution
            self.solutions.append(["".join(self.chessBoard[i]) for i in range(self.sizeofBlock)])
            return True  # If only one solution is needed, this stops further search
        
        for col in range(self.sizeofBlock):
            # Skip columns and diagonals already under attack
            if self.columns[col] or self.diagonals[row + col] or self.antiDiagonals[row - col + (self.sizeofBlock - 1)]:
                continue
            
            # Place a queen and mark the column/diagonals as occupied
            self.chessBoard[row][col] = 'Q'
            self.columns[col] = self.diagonals[row + col] = self.antiDiagonals[row - col + (self.sizeofBlock - 1)] = 1
            
            # Recur for the next row
            self.DepthFirstSearch(row + 1)
            
            # Backtrack: remove the queen and unmark the column/diagonals
            self.chessBoard[row][col] = 'x'
            self.columns[col] = self.diagonals[row + col] = self.antiDiagonals[row - col + (self.sizeofBlock - 1)] = 0
        
        return False

    def Solve(self):
        """
        Solve the N-Queens problem and display all solutions.
        """
        self.DepthFirstSearch()
        print(f"Total Solutions for {self.sizeofBlock}x{self.sizeofBlock}: {len(self.solutions)}")
        for solution in self.solutions:
            self.DisplayBoard(solution)
