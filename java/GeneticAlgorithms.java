import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class GeneticAlgorithms 
{

    private int blockSize; // Size of the board (NxN)
    private final int POPULATIONSIZE = 100; // Number of boards in each generation
    private final int GENERATIONS = 100000; // Maximum number of generations
    private final double MUTATIONRATE = 0.01; // Probability of mutation
    private final int ELITESIZE = 20; // Number of top boards preserved in each generation

    // Constructor to initialize the block size (board size)
    public GeneticAlgorithms(int sizeOfBlock) 
    {
        this.blockSize = sizeOfBlock;
    }

    /**
     * Displays a chessboard based on the board configuration.
     *
     * @param board A list representing the column position of queens for each row.
     */
    public void DisplayBoard(List<Integer> board) 
    {
        for (int row : board) 
        {
            for (int i = 0; i < blockSize; i++)
                System.out.print(i == row ? "Q " : ". ");
            System.out.println();
        }
    }

    /**
     * Calculates the fitness of a board.
     * Fitness is defined as the maximum number of non-attacking pairs of queens.
     *
     * @param board The board configuration.
     * @return The fitness score of the board.
     */
    public int Fitness(List<Integer> board) 
    {
        int n = board.size();
        int maxPairs = n * (n - 1) / 2; // Maximum number of pairs of queens
        int attackingPairs = 0;

        // Count the number of pairs of queens attacking each other
        for (int i = 0; i < n; i++) 
            for (int j = i + 1; j < n; j++)
                if (Math.abs(board.get(i) - board.get(j)) == Math.abs(i - j))
                    attackingPairs++;

        return maxPairs - attackingPairs; // Non-attacking pairs
    }

    /**
     * Generates the initial population of boards.
     *
     * @param populationSize The number of boards to generate.
     * @return A list of boards representing the initial population.
     */
    public List<List<Integer>> GeneratePopulation(int populationSize) 
    {
        List<List<Integer>> population = new ArrayList<>();
        Random rand = new Random();

        for (int i = 0; i < populationSize; i++) 
        {
            List<Integer> board = new ArrayList<>();
            for (int j = 0; j < blockSize; j++) 
            {
                board.add(j);
            }
            Collections.shuffle(board, rand); // Shuffle to create a random board
            population.add(board);
        }
        return population;
    }

    /**
     * Performs crossover between two parent boards to produce a child board.
     *
     * @param parent1 The first parent board.
     * @param parent2 The second parent board.
     * @return The child board.
     */
    public List<Integer> Crossover(List<Integer> parent1, List<Integer> parent2) {
        Random rand = new Random();
        int point1 = rand.nextInt(blockSize - 1); // Random start
        int point2 = rand.nextInt(blockSize - point1) + point1; // Random end
    
        List<Integer> child = new ArrayList<>(Collections.nCopies(blockSize, -1));
        // Copy a segment from parent1
        for (int i = point1; i <= point2; i++) {
            child.set(i, parent1.get(i));
        }
    
        // Fill remaining values from parent2 in order
        int currentIndex = 0;
        for (int value : parent2) {
            if (!child.contains(value)) {
                while (child.get(currentIndex) != -1) {
                    currentIndex++;
                }
                child.set(currentIndex, value);
            }
        }
    
        return child;
    }
    /**
     * Performs mutation on a board with a given mutation rate.
     *
     * @param board The board to mutate.
     * @param mutationRate The probability of mutation.
     * @return The mutated board.
     */
    public List<Integer> Mutate(List<Integer> board, double mutationRate) {
        Random rand = new Random();
        if (rand.nextDouble() < mutationRate) {
            int i = rand.nextInt(blockSize);
            int j = rand.nextInt(blockSize);
            Collections.swap(board, i, j); // Swap ensures a valid permutation
        }
        return board;
    }
    

    /**
     * Creates a new generation of boards.
     *
     * @param population The current population.
     * @param fitnessScores The fitness scores of the current population.
     * @param populationSize The size of the new population.
     * @param eliteSize The number of elite boards to carry over.
     * @param mutationRate The mutation rate.
     * @return The next generation of boards.
     */
    public List<List<Integer>> CreateNewGeneration(
            List<List<Integer>> population, 
            List<Integer> fitnessScores, 
            int populationSize, 
            int eliteSize, 
            double mutationRate) 
    {

        List<List<Integer>> nextGeneration = new ArrayList<>();
        List<List<Integer>> elites = new ArrayList<>();

        // Rank population by fitness (descending)
        List<Integer> indices = new ArrayList<>();
        for (int i = 0; i < population.size(); i++) 
            indices.add(i);
        indices.sort((a, b) -> fitnessScores.get(b) - fitnessScores.get(a));

        // Add elite boards to the next generation
        for (int i = 0; i < eliteSize; i++) 
            elites.add(population.get(indices.get(i)));
        nextGeneration.addAll(elites);

        Random rand = new Random();
        // Fill the rest of the population with offspring
        while (nextGeneration.size() < populationSize) 
        {
            List<Integer> parent1 = population.get(rand.nextInt(population.size()));
            List<Integer> parent2 = population.get(rand.nextInt(population.size()));
            List<Integer> child = Mutate(Crossover(parent1, parent2), mutationRate);
            nextGeneration.add(child);
        }
        return nextGeneration;
    }

    /**
     * Runs the genetic algorithm to solve the N-Queens problem.
     *
     * @return true if a solution is found, false otherwise.
     */
    public boolean Solve() 
    {
        List<List<Integer>> population = GeneratePopulation(POPULATIONSIZE);

        for (int generation = 0; generation < GENERATIONS; generation++) 
        {
            List<Integer> fitnessScores = new ArrayList<>();
            for (List<Integer> board : population) 
            {
                fitnessScores.add(Fitness(board)); // Calculate fitness for each board
            }

            int maxFitness = Collections.max(fitnessScores); // Best fitness in the population

            // Check if a perfect solution is found
            if (maxFitness == blockSize * (blockSize - 1) / 2) 
            {
                System.out.println("Solution found in generation " + generation + "\n");
                DisplayBoard(population.get(fitnessScores.indexOf(maxFitness)));
                return true;
            }

            // Create the next generation
            population = CreateNewGeneration(population, fitnessScores, POPULATIONSIZE, ELITESIZE, MUTATIONRATE);
        }

        System.out.println("No solution found.");
        return false;
    }
}
