import heapq
import random

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]
    cost = {start: 0}
    parent = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost[current] + 1

                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (priority, (nx, ny)))
                    parent[(nx, ny)] = current

    return None


def add_dynamic_obstacle(grid):
    rows, cols = len(grid), len(grid[0])
    x, y = random.randint(0, rows-1), random.randint(0, cols-1)
    if grid[x][y] == 0:
        grid[x][y] = 1
        print(f"New obstacle appeared at {(x, y)}")


def dynamic_navigation(grid, start, goal):
    current = start
    path_taken = [current]

    while current != goal:
        path = astar(grid, current, goal)

        if not path:
            print("No path found!")
            return path_taken

        # Move step by step
        for step in path[1:]:
            # Randomly introduce new obstacle
            if random.random() < 0.3:
                add_dynamic_obstacle(grid)

                # If next step becomes blocked → replan
                if grid[step[0]][step[1]] == 1:
                    print("Path blocked! Replanning...")
                    break

            current = step
            path_taken.append(current)

            if current == goal:
                print("Reached goal!")
                return path_taken

    return path_taken


# Example grid
grid = [
    [0,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,0,0]
]

start = (0,0)
goal = (3,3)

result = dynamic_navigation(grid, start, goal)
print("Path taken:", result)