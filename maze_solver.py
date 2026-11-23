import heapq

# 0 = Empty cell, 1 = Wall
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)

            r, c = neighbor

            if (0 <= r < rows and 0 <= c < cols
                    and maze[r][c] == 0):

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))

    return None

def display_maze(maze, path, start, goal):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            position = (r, c)

            if position == start:
                print("S", end=" ")
            elif position == goal:
                print("G", end=" ")
            elif path and position in path:
                print("*", end=" ")
            elif maze[r][c] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

path = astar(maze, start, goal)

print("MAZE SOLVER USING A* SEARCH")
print("S = Start, G = Goal, # = Wall, * = Shortest Path")
print()

if path:
    print("Shortest path found!")
    print("Path length:", len(path) - 1)
    display_maze(maze, path, start, goal)
else:
    print("No path found. Goal is unreachable.")
    display_maze(maze, None, start, goal)
