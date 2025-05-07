import heapq

# Define the grid
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Directions for moving in 4 possible directions (up, down, left, right)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Heuristic: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm implementation
def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))  # f, g, (x, y)
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current_g, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = current_g + 1  # Assume each move has a cost of 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))

    return None  # If no path is found

# Example usage
start = (0, 0)  # Start position (row, col)
goal = (4, 4)   # Goal position (row, col)

path = astar(start, goal)
print("Path found:", path)
