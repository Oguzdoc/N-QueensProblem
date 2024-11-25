import random
# Genetic Algorithm Implementation
class GeneticAlgorithms:

    def __init__(self,sizeOfBlock) -> None:
        """
        Initialize the GeneticAlgorithms class with a given board size.
        """    
        self.blockSize = sizeOfBlock
        pass
    
    def DisplayBoard(self,board):
        """
        Display the given board in a human-readable format.
        - board: List of integers representing the queen positions.
        """        
        n = len(board)
        for row in board:
            print(" ".join("Q" if i == row else "x" for i in range(n)))
            
    def Fitness(self, board):
        """
        Calculate the fitness score of a board configuration.
        - board: List of integers representing the queen positions.
        Returns the number of non-attacking pairs of queens.
        """        
        n = len(board)
        maxPairs = n * (n - 1) // 2
        attackingPairs = 0
        
         # Count attacking pairs (queens on the same diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(board[i] - board[j]) == abs(i - j):
                    attackingPairs += 1
        return maxPairs - attackingPairs
     
    def GeneratePopulation(self,populationSize):
        """
        Generate an initial random population of board configurations.
        - populationSize: Number of individuals in the population.
        Returns a list of random boards.
        """        
        return [random.sample(range(self.blockSize), self.blockSize) for _ in range(populationSize)]
    
    def Crossover(self,parent1, parent2):
        """
        Perform crossover between two parents to produce an offspring.
        - parent1, parent2: Parent boards.
        Returns a new board configuration.
        """        
        n = len(parent1)
        point = random.randint(1, n - 1)
        return parent1[:point] + parent2[point:]
    
    def Mutate(self,board, mutationRate):
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
        combined = list(zip(population, fitnessScores))
        combined.sort(key=lambda x: x[1], reverse=True)
        elites = [individual for individual, _ in combined[:eliteSize]]
        nextGeneration = elites[:]

        # Fill the rest of the population
        while len(nextGeneration) < populationSize:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = self.Crossover(parent1, parent2)
            child = self.Mutate(child, mutationRate)
            nextGeneration.append(child)

        return nextGeneration
    
    def GeneticAlgorithm(self, populationSize, generations, mutationRate,eliteSize = 5) ->bool:
        """
        Run the genetic algorithm to solve the N-Queens problem.
        - populationSize: Number of individuals in the population.
        - generations: Maximum number of generations.
        - mutationRate: Probability of mutation.
        - eliteSize: Number of top individuals to preserve.
        Returns True if a solution is found, otherwise False.
        """        
        population = self.GeneratePopulation(populationSize)

        for generation in range(generations):
            fitnessScores = [self.Fitness(board) for board in population]
            maxFitness = max(fitnessScores)
            # Check if a perfect solution is found
            if maxFitness == self.blockSize * (self.blockSize - 1) // 2:
                print(f"Solution found in generation {generation}\n")
                self.DisplayBoard(population[fitnessScores.index(maxFitness)])
                return True
            # Create the next generation
            population = self.CreateNewGeneration(population, fitnessScores, populationSize, eliteSize, mutationRate)

        print("No solution found.")
        return False
    
