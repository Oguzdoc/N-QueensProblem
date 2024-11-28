import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DepthFirstSearch {

    private int boardSize;              // The size of the chessboard (N x N)
    private List<int[]> solutions;      // List to store all valid solutions

    /**
     * Constructor for DepthFirstSearch class.
     * Initializes the board size and the solutions list.
     *
     * @param boardSize The size of the chessboard (N x N).
     */
    public DepthFirstSearch(int boardSize) {
        this.boardSize = boardSize;
        this.solutions = new ArrayList<>();
    }

    /**
     * Displays the chessboard with the queen positions for a given board state.
     *
     * @param board The array representing queen positions where board[row] = column.
     */
    private void DisplayBoard(int[] board) {
        for (int row = 0; row < this.boardSize; row++) {
            for (int col = 0; col < this.boardSize; col++) {
                // Print "Q" for a queen and "." for an empty space
                if (board[row] == col)
                    System.out.print("Q ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
        System.out.println(); // Separate solutions
    }

    /**
     * Checks if placing a queen at (row, col) is safe (no conflicts).
     *
     * @param board The current state of the board.
     * @param row   The row to check.
     * @param col   The column to check.
     * @return true if the position is safe, false otherwise.
     */
    private boolean IsSafe(int[] board, int row, int col) {
        for (int i = 0; i < row; i++) {
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
     */
    private void DepthFirstSearchAlgorithm(int[] board, int row) {
        // Base case: all queens are placed successfully
        if (row == this.boardSize) {
            solutions.add(board.clone()); // Store the solution
            return;
        }

        // Try placing a queen in each column of the current row
        for (int col = 0; col < this.boardSize; col++) {
            if (IsSafe(board, row, col)) {
                board[row] = col; // Place the queen in this column
                DepthFirstSearchAlgorithm(board, row + 1); // Recur to place the next queen
                board[row] = -1; // Backtrack (remove the queen)
            }
        }
    }

    /**
     * Solves the N-Queens problem using DFS and displays all solutions.
     */
    public void Solve() {
        int[] board = new int[this.boardSize]; // Array to represent the board (column positions for each row)
        Arrays.fill(board, -1); // Initialize with -1 (no queen placed)

        DepthFirstSearchAlgorithm(board, 0); // Start DFS from row 0
        
        System.out.println("Total Solutions: " + solutions.size());
        for (int[] solution : solutions) {
            DisplayBoard(solution); // Display each solution
        }
    }
}
