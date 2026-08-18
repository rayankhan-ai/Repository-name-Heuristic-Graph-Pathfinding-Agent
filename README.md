# Heuristic Graph Pathfinding Agent Search Engine

## Project Overview

The Heuristic Graph Pathfinding Agent Search Engine is an intelligent path optimization system developed using Python and Streamlit. The project enables virtual agents to navigate complex grid-based mazes by finding the shortest path between a starting point and a destination while avoiding obstacles.

This project implements two well-known pathfinding algorithms, Dijkstra's Algorithm and A* Search, completely from scratch. It also evaluates and compares their performance using different metrics, including runtime, step count, and expanded node density.

---

## Project Objectives

- Develop an intelligent pathfinding framework.
- Implement heuristic search algorithms from scratch.
- Generate complex grid mazes with random obstacles.
- Compare the performance of different pathfinding algorithms.
- Track important performance metrics.
- Visualize path optimization.
- Export visualization logs.
- Build an interactive Streamlit web application.

---

## Features

- Random grid maze generation
- Adjustable grid size
- Configurable obstacle density
- Dijkstra's Algorithm implementation
- A* Search Algorithm implementation
- Shortest-path calculation
- Runtime measurement
- Step count tracking
- Expanded node tracking
- Expanded node density calculation
- Path visualization
- CSV log export
- Comparison chart generation
- Interactive Streamlit interface

---

## Algorithms Used

### Dijkstra's Algorithm

Dijkstra's Algorithm is an uninformed search algorithm that explores all possible paths and guarantees the shortest path between the start and destination nodes.

### A* Search Algorithm

A* Search is a heuristic-based algorithm that combines the actual path cost with an estimated cost to the goal. In this project, the Manhattan Distance heuristic is used to improve search efficiency.

---

## Performance Metrics

The following metrics are used to evaluate both algorithms:

| Metric | Description |
| --- | --- |
| Runtime | Time required to find the path |
| Step Count | Number of steps in the shortest path |
| Expanded Nodes | Total number of explored nodes |
| Expanded Node Density | Expanded nodes divided by the total number of grid cells |

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Heapq
- Streamlit

---

## Project Structure

```text
Heuristic_Graph_Pathfinding_Agent

├── app.py
├── requirements.txt

└── output
    ├── pathfinding_metrics.csv
    └── pathfinding_comparison.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rayankhan-ai/Repository-name-Heuristic-Graph-Pathfinding-Agent.git
```

Move to the project directory:

```bash
cd Repository-name-Heuristic-Graph-Pathfinding-Agent
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Output Files

The project automatically generates the following files:

```text
output/

├── pathfinding_metrics.csv
└── pathfinding_comparison.png
```

---

## Streamlit Deployment

The application can be deployed using Streamlit Community Cloud.

1. Upload the project to GitHub.
2. Connect the GitHub repository to Streamlit Cloud.
3. Select `app.py` as the main file.
4. Deploy the application.

---

## Future Improvements

- Add Q-Learning implementation.
- Add support for diagonal movement.
- Add multiple heuristic functions.
- Add custom maze uploads.
- Add real-time agent animation.

---

## Author

**Rayan Ahmad**

Software Engineering Student

University of Malakand

---

## License

This project is intended for educational and internship purposes.