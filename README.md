# Mine Detection and Navigation Game

This is a simple mine detection and navigation game where an AI agent is tasked with navigating a 5x5 grid to locate a gold mine while avoiding mines hidden in some cells. The AI agent uses logical inference and search algorithms to safely navigate the grid and infer the location of the gold mine.

## Features

- A rule-based AI agent that uses logical inference and search algorithms
- A knowledge base (KB) for handling information about the grid cells
- A SAT solver (Glucose3) to perform logical inference
- Breadth-First Search (BFS) and depth-first search (DFS) algorithms for navigation

## Getting Started

### Prerequisites

To run the game, you will need Python 3 and the PySAT library. You can install PySAT using pip:

```
pip install python-sat
```

### Running the game

1. Clone the repository or download the source code.
2. Navigate to the folder containing the source code.
3. Run the `main.py` file using Python:

```
python main.py
```

The AI agent will navigate the grid, and the output will show the agent's actions, perceptions, and inferred location of the gold mine.

## How it works

The AI agent navigates the 5x5 grid by taking actions (moving up, down, left, or right) and perceiving its surroundings. The agent can perceive the number of mines in the adjacent cells but cannot directly perceive the location of the gold mine.

The agent uses a knowledge base (KB) to represent information about the safety status of each cell. As it navigates the grid and perceives its environment, it updates the KB with new information. The SAT solver (Glucose3) is used to determine if any cells are unambiguously safe or contain a mine, allowing the agent to make informed decisions about its actions.

A combination of Breadth-First Search (BFS) and depth-first search (DFS) algorithms is used to efficiently navigate the grid. The agent maintains a queue of safe cells to visit and traverses the grid using BFS. DFS is employed to backtrack and find the shortest path to the next safe cell when necessary.

## License

This project is open-source and available for educational purposes. Please acknowledge the source if you use or adapt the code in your projects.

## Topics

- `artificial-intelligence`
- `logical-inference`
- `knowledge-representation`
- `sat-solver`
- `search-algorithms`
- `breadth-first-search`
- `depth-first-search`
- `grid-based-environment`
- `python`
- `educational-project`
- `mine-detection`
- `navigation`