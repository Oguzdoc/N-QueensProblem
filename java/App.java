public class App 
{
    public static void main(String[] args) throws Exception 
    {
        // Header message
        System.out.println("N-Queens Problem");

        // Solving the problem using Depth First Search (DFS) for a 10x10 board
        System.out.println("Depth First Search 10x10");
        DepthFirstSearch depthFirstSearch = new DepthFirstSearch(10); // Initialize with board size 10x10
        long startTime = System.nanoTime(); // Record start time
        depthFirstSearch.Solve(); // Solve the problem using DFS
        long endTime = System.nanoTime(); // Record end time
        System.out.println("Execution time : " + ((double)(endTime - startTime) / 1_000_000_000.0) + " sec.");

        // Solving the problem using Genetic Algorithms (GA) for a 10x10 board
        GeneticAlgorithms geneticAlgorithms = new GeneticAlgorithms(10); // Initialize with board size 10x10
        System.out.println("Genetic Algorithms 10x10");
        startTime = System.nanoTime(); // Record start time
        geneticAlgorithms.Solve(); // Solve the problem using GA
        endTime = System.nanoTime(); // Record end time
        System.out.println("Execution time : " + ((double)(endTime - startTime) / 1_000_000_000.0) + " sec.");

        // Solving the problem using Genetic Algorithms for a 50x50 board
        geneticAlgorithms = new GeneticAlgorithms(50); // Initialize with board size 50x50
        startTime = System.nanoTime(); // Record start time
        System.out.println("Genetic Algorithms 50x50");
        geneticAlgorithms.Solve(); // Solve the problem using GA
        endTime = System.nanoTime(); // Record end time
        System.out.println("Execution time : " + ((double)(endTime - startTime) / 1_000_000_000.0) + " sec.");

        // Solving the problem using Genetic Algorithms for a 100x100 board
        geneticAlgorithms = new GeneticAlgorithms(100); // Initialize with board size 100x100
        startTime = System.nanoTime(); // Record start time
        System.out.println("Genetic Algorithms 100x100");
        geneticAlgorithms.Solve(); // Solve the problem using GA
        endTime = System.nanoTime(); // Record end time
        System.out.println("Execution time : " + ((double)(endTime - startTime) / 1_000_000_000.0) + " sec.");
    }
}
