# N-Queens Problem Solver  
This repository provides implementations of the N-Queens problem using Depth First Search (DFS) and Genetic Algorithms (GA) in **Python** and **Java**.  

## Problem Statement  
The N-Queens problem involves placing N queens on an NxN chessboard such that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal.  

## Algorithms Implemented  
### 1. **Depth First Search (DFS)**  
DFS is used with backtracking to explore all possible placements of queens on the chessboard. It guarantees finding all solutions but can be computationally expensive for larger board sizes.  

### 2. **Genetic Algorithm (GA)**  
GA uses evolutionary principles such as selection, crossover, and mutation to generate solutions. While it doesn't guarantee finding all solutions, it is efficient and scalable for larger board sizes.  

## Features  
- Implementations in **Python** and **Java**.  
- Comparison of execution times for both algorithms.  
- Demonstrates the performance differences between deterministic (DFS) and probabilistic (GA) approaches.  

## Folder Structure  
```plaintext
.
├── java/
│   ├── App.java                 # Entry point for Java implementations
│   ├── DepthFirstSearch.java    # Java implementation of DFS
│   ├── GeneticAlgorithms.java   # Java implementation of GA
├── python/
│   ├── ExhaustiveSearch.py      # Python implementation of DFS
│   ├── GeneticAlgorithms.py     # Python implementation of GA
│   └── main.py                  # Entry point for Python implementations
├── README.md                    # Documentation
