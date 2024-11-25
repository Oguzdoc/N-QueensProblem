import java.util.Arrays;

public class DepthFirstSearch 
{
    private int _boardSize = 0; // The size of the chessboard (number of rows and columns)
    private int[] _solutions;  // Array to store the positions of queens in a valid solution

    /**
     * Constructor for DepthFirstSearch class.
     * Initializes the board size and the solutions array.
     *
     * @param boardSize The size of the chessboard (N x N).
     */
    public DepthFirstSearch(int boardSize) 
    {
        this._boardSize = boardSize;
        this._solutions = new int[this._boardSize];
    }

    /**
     * Displays the chessboard with the queen positions for a given board state.
     *
     * @param board The array representing queen positions where board[row] = column.
     */
    private void DisplayBoard(int[] board) 
    {
        for (int row = 0; row < this._boardSize; row++) 
        {
            for (int col = 0; col < this._boardSize; col++) 
            {
                // Print "Q" for a queen and "." for an empty space
                if (board[row] == col)
                    System.out.printf("Q ");
                else
                    System.out.printf(". ");
            }
            System.out.println();
        }
    }

    /**
     * Checks if placing a queen at (row, col) is safe (no conflicts).
     *
     * @param board The current state of the board.
     * @param row   The row to check.
     * @param col   The column to check.
     * @return true if the position is safe, false otherwise.
     */
    private boolean IsSafe(int[] board, int row, int col) 
    {
        for (int i = 0; i < row; i++) 
        {
            // Check for column conflicts
            if (board[i] == col)
                return false;

            // Check for diagonal conflicts
            if (Math.abs(board[i] - col) == Math.abs(i - row))
                return false;
        }
        return true; // No conflicts, position is safe
    }

    /**
     * Depth First Search algorithm to solve the N-Queens problem.
     *
     * @param board The current state of the board.
     * @param row   The current row to place a queen.
     * @return true if a solution is found, false otherwise.
     */
    private boolean DepthFirstSearchAlgorithm(int[] board, int row) 
    {
        // Base case: all queens are placed successfully
        if (row == this._boardSize) 
        {
            this._solutions = board; // Store the solution
            return true;
        }

        // Try placing a queen in each column of the current row
        for (int col = 0; col < this._boardSize; col++) 
        {
            if (IsSafe(board, row, col)) 
            {
                board[row] = col; // Place the queen in this column
                // Recur to place the next queen
                if (DepthFirstSearchAlgorithm(board, row + 1))
                    return true;
                board[row] = -1; // Backtrack (remove the queen)
            }
        }
        return false; // No valid positions in this row
    }

    /**
     * Solves the N-Queens problem using DFS and displays the solution.
     */
    public void Solve() 
    {
        int[] board = new int[this._boardSize]; // Array to represent the board (column positions for each row)
        Arrays.fill(board, -1); // Initialize with -1 (no queen placed)

        DepthFirstSearchAlgorithm(board, 0); // Start DFS from row 0
        DisplayBoard(this._solutions); // Display the solution
    }
}
