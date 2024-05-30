# GraphBased-PathPlanningAlgo

Practice project to master the concepts of path planning algorithms.

## First Step: Create a Maze using Kruskal's Algorithm

This project involves creating a maze using Kruskal's algorithm. The maze is displayed using Pygame.

### First we must think of how much do we want to set the width and height of the display and cell size

**Determine Grid Length**: Set the grid length for the first row, first column, and so on. 

```python
for row in range(rows):
    for col in range(cols):
        x = col * cell_size
        y = row * cell_size
      
