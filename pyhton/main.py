
import time
from ExhaustiveSearch import ExhaustiveSearch
from GeneticAlgorithms import GeneticAlgorithms

POPULATIONSIZE = 100
GENERATIONS = 5000
MUTATIONRATE = 0.2


print("\n***N-Queens Problem*****\n")
exhaustiveSearch = ExhaustiveSearch(10)

print("***Depth First Search*****\n")
startTime = time.time()
exhaustiveSearch.DepthFirstSearch()
endTime = time.time()
elapsedTime = endTime - startTime

print(f"\nFunction execution time: {elapsedTime:.6f} seconds\n")

print("***Genetic Algorithm*****\n")

print("***Genetic Algorithm For 10x10 Board*****\n")
geneticAlgorithms = GeneticAlgorithms(10)

startTime = time.time()
geneticAlgorithms.GeneticAlgorithm(POPULATIONSIZE,GENERATIONS,MUTATIONRATE)
endTime = time.time()
print(f"Function execution time: {endTime-startTime:.6f} seconds\n")

print("***Genetic Algorithm For 50x50 Board*****\n")
geneticAlgorithms = GeneticAlgorithms(50)

startTime = time.time()
geneticAlgorithms.GeneticAlgorithm(POPULATIONSIZE,GENERATIONS,MUTATIONRATE)
endTime = time.time()
print(f"Function execution time: {endTime-startTime:.6f} seconds\n")

print("***Genetic Algorithm For 100x100 Board*****\n")
geneticAlgorithms = GeneticAlgorithms(100)

startTime = time.time()
geneticAlgorithms.GeneticAlgorithm(POPULATIONSIZE,GENERATIONS,MUTATIONRATE)
endTime = time.time()
print(f"Function execution time: {endTime-startTime:.6f} seconds\n")