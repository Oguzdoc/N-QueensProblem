import random

class GeneticAlgorithms:

    def __init__(self, sizeOfBlock):
        """
        Initialize the GeneticAlgorithms class with a given board size.
        """
        self.blockSize = sizeOfBlock

    def DisplayBoard(self, board):
        """
        Display the given board in a human-readable format.
        - board: List of integers representing the queen positions.
        """
        for row in board:
            print(" ".join("Q " if i == row else "x " for i in range(self.blockSize)))
        print()

    def Fitness(self, board):
        """
        Calculate the fitness score of a board configuration.
        - board: List of integers representing the queen positions.
        Returns the number of non-attacking pairs of queens.
        """
        n = len(board)
        maxPairs = n * (n - 1) // 2  # Maximum number of pairs
        attackingPairs = 0

        # Count attacking pairs (diagonal attacks)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(board[i] - board[j]) == abs(i - j):
                    attackingPairs += 1

        return maxPairs - attackingPairs

    def GeneratePopulation(self, populationSize):
        """
        Generate an initial random population of board configurations.
        - populationSize: Number of individuals in the population.
        Returns a list of random boards.
        """
        population = []
        for _ in range(populationSize):
            board = list(range(self.blockSize))
            random.shuffle(board)
            population.append(board)
        return population

    def Crossover(self, parent1, parent2):
        """
        Perform crossover between two parents to produce an offspring.
        - parent1, parent2: Parent boards.
        Returns a new board configuration.
        """
        point1 = random.randint(0, self.blockSize - 2)
        point2 = random.randint(point1 + 1, self.blockSize - 1)
        child = [-1] * self.blockSize

        # Copy a segment from parent1
        for i in range(point1, point2 + 1):
            child[i] = parent1[i]

        # Fill remaining values from parent2 in order
        current_index = 0
        for value in parent2:
            if value not in child:
                while child[current_index] != -1:
                    current_index += 1
                child[current_index] = value

        return child

    def Mutate(self, board, mutationRate):
        """
        Perform mutation on a board based on the mutation rate.
        - board: Board to mutate.
        - mutationRate: Probability of mutation.
        Returns the mutated board.
        """
        if random.random() < mutationRate:
            i, j = random.sample(range(len(board)), 2)
            board[i], board[j] = board[j], board[i]
        return board

    def CreateNewGeneration(self, population, fitnessScores, populationSize, eliteSize, mutationRate):
        """
        Create a new generation by selecting elites and performing crossover and mutation.
        - population: Current population of boards.
        - fitnessScores: Fitness scores of the current population.
        - populationSize: Size of the population.
        - eliteSize: Number of top individuals to preserve.
        - mutationRate: Probability of mutation.
        Returns a new population.
        """
        # Sort population by fitness in descending order
        sorted_population = [board for _, board in sorted(zip(fitnessScores, population), reverse=True)]
        elites = sorted_population[:eliteSize]
        nextGeneration = elites[:]

        # Fill the rest of the population
        while len(nextGeneration) < populationSize:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = self.Crossover(parent1, parent2)
            child = self.Mutate(child, mutationRate)
            nextGeneration.append(child)

        return nextGeneration

    def Solve(self,POPULATION_SIZE,GENERATIONS,MUTATION_RATE,ELITE_SIZE = 20):
        """
        Run the genetic algorithm to solve the N-Queens problem.
        Returns True if a solution is found, otherwise False.
        """
        population = self.GeneratePopulation(POPULATION_SIZE)

        for generation in range(GENERATIONS):
            fitnessScores = [self.Fitness(board) for board in population]
            maxFitness = max(fitnessScores)

            # Check if a perfect solution is found
            if maxFitness == self.blockSize * (self.blockSize - 1) // 2:
                print(f"Solution found in generation {generation}\n")
                self.DisplayBoard(population[fitnessScores.index(maxFitness)])
                return True

            # Create the next generation
            population = self.CreateNewGeneration(population, fitnessScores, POPULATION_SIZE, ELITE_SIZE, MUTATION_RATE)

        print("No solution found.")
        return False


