from collections import deque

def flood_fill_bfs(grid, x, y, old_color, new_color):
    rows = len(grid)
    cols = len(grid[0])

    if grid[x][y] != old_color:
        return

    queue = deque()
    queue.append((x, y))
    grid[x][y] = new_color

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == old_color:
                grid[nx][ny] = new_color
                queue.append((nx, ny))


# Example usage
maze = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
]
print("Before Flood Fill")
for row in maze:
    print(row)
    
flood_fill_bfs(maze, 0, 0, 1, 2)
print("After Flood Fill")
for row in maze:
    print(row)
