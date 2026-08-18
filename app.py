# ==========================================================
# Heuristic Graph Pathfinding Agent Search Engine
# Streamlit Web Application
# ==========================================================

# Import required libraries

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import heapq
import random
import time
import pandas as pd

# Set the page configuration

st.set_page_config(

    page_title="Pathfinding Agent Search Engine",

    layout="wide"

)

# Application title

st.title(

    "Heuristic Graph Pathfinding Agent Search Engine"

)

# Sidebar controls

st.sidebar.header(

    "Grid Settings"

)

grid_size = st.sidebar.slider(

    "Grid Size",

    10,

    50,

    20

)

obstacle_percentage = st.sidebar.slider(

    "Obstacle Percentage",

    0.1,

    0.5,

    0.25

)

# Generate the grid

grid = np.zeros(

    (grid_size, grid_size)

)

number_of_obstacles = int(

    grid_size

    *

    grid_size

    *

    obstacle_percentage

)

for _ in range(

    number_of_obstacles

):

    row = random.randint(

        0,

        grid_size - 1

    )

    column = random.randint(

        0,

        grid_size - 1

    )

    grid[row, column] = 1

# Define the start and goal nodes

start = (

    0,

    0

)

goal = (

    grid_size - 1,

    grid_size - 1

)

grid[start] = 0

grid[goal] = 0

# Movement directions

directions = [

    (0, 1),

    (1, 0),

    (0, -1),

    (-1, 0)

]

# Neighbor function

def get_neighbors(position):

    neighbors = []

    row, column = position

    for dr, dc in directions:

        new_row = row + dr

        new_column = column + dc

        if (

            0 <= new_row < grid_size

            and

            0 <= new_column < grid_size

        ):

            if grid[new_row, new_column] == 0:

                neighbors.append(

                    (new_row, new_column)

                )

    return neighbors

# Dijkstra algorithm

def dijkstra(start, goal):

    queue = []

    heapq.heappush(

        queue,

        (0, start)

    )

    distances = {

        start: 0

    }

    previous_nodes = {}

    expanded_nodes = 0

    while queue:

        current_distance, current_node = heapq.heappop(

            queue

        )

        expanded_nodes += 1

        if current_node == goal:

            break

        for neighbor in get_neighbors(

            current_node

        ):

            distance = current_distance + 1

            if (

                neighbor not in distances

                or

                distance < distances[neighbor]

            ):

                distances[neighbor] = distance

                previous_nodes[neighbor] = current_node

                heapq.heappush(

                    queue,

                    (distance, neighbor)

                )

    path = []

    current = goal

    while current in previous_nodes:

        path.append(current)

        current = previous_nodes[current]

    path.append(start)

    path.reverse()

    return (

        path,

        expanded_nodes

    )

# Heuristic function

def heuristic(node, goal):

    return (

        abs(node[0] - goal[0])

        +

        abs(node[1] - goal[1])

    )

# A* algorithm

def astar(start, goal):

    queue = []

    heapq.heappush(

        queue,

        (0, start)

    )

    g_score = {

        start: 0

    }

    previous_nodes = {}

    expanded_nodes = 0

    while queue:

        _, current_node = heapq.heappop(

            queue

        )

        expanded_nodes += 1

        if current_node == goal:

            break

        for neighbor in get_neighbors(

            current_node

        ):

            tentative_g_score = (

                g_score[current_node] + 1

            )

            if (

                neighbor not in g_score

                or

                tentative_g_score < g_score[neighbor]

            ):

                g_score[neighbor] = tentative_g_score

                previous_nodes[neighbor] = current_node

                f_score = (

                    tentative_g_score

                    +

                    heuristic(

                        neighbor,

                        goal

                    )

                )

                heapq.heappush(

                    queue,

                    (f_score, neighbor)

                )

    path = []

    current = goal

    while current in previous_nodes:

        path.append(current)

        current = previous_nodes[current]

    path.append(start)

    path.reverse()

    return (

        path,

        expanded_nodes

    )

# Run the algorithms

start_time = time.perf_counter()

dijkstra_path, dijkstra_nodes = dijkstra(

    start,

    goal

)

dijkstra_runtime = (

    time.perf_counter() - start_time

)

start_time = time.perf_counter()

astar_path, astar_nodes = astar(

    start,

    goal

)

astar_runtime = (

    time.perf_counter() - start_time

)

# Visualization

visual_grid = grid.copy()

for row, column in astar_path:

    visual_grid[row, column] = 2

fig, ax = plt.subplots(

    figsize=(8, 8)

)

ax.imshow(

    visual_grid

)

ax.set_title(

    "A* Path Visualization"

)

st.pyplot(

    fig

)

# Metrics table

metrics = pd.DataFrame(

    {

        "Algorithm": [

            "Dijkstra",

            "A*"

        ],

        "Runtime": [

            dijkstra_runtime,

            astar_runtime

        ],

        "Steps": [

            len(dijkstra_path),

            len(astar_path)

        ],

        "Expanded Nodes": [

            dijkstra_nodes,

            astar_nodes

        ]

    }

)

st.subheader(

    "Performance Metrics"

)

st.dataframe(

    metrics
)