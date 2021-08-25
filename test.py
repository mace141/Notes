from collections import deque

def best_bridge(grid):
  first_island = set()
  land_positions = []
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'L':
        scope_out_land(grid, land_positions, first_island, r, c)
        break
    else:
      continue 
    break

  bridge_length = float('inf')
  for pos in land_positions:
    y, x = pos
    length = bridge(grid, first_island, y, x)
    bridge_length = length if length < bridge_length else bridge_length
  return bridge_length

def scope_out_land(grid, land_positions, first_island, r, c):
  if (r, c) in first_island or grid[r][c] == 'W':
    return
  first_island.add((r, c))
  land_positions.append([r, c])
  deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  for delta in deltas:
    [new_row, new_col], valid_pos = in_bounds(grid, delta, r, c)
    if valid_pos:
      scope_out_land(grid, land_positions, first_island, new_row, new_col)

def bridge(grid, first_island, row, col):
  deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  visited = set()
  queue = deque([[row, col, -1]])
  while queue:
    y, x, dst = queue.popleft()
    if grid[y][x] == 'L' and (y, x) not in first_island:
      return dst
    visited.add((y, x))
    for delta in deltas:
      [new_row, new_col], valid_pos = in_bounds(grid, delta, y, x)
      pos = (new_row, new_col)
      if valid_pos and pos not in visited and pos not in first_island:
        queue.append([new_row, new_col, dst + 1])
  return float('inf')

def in_bounds(grid, delta, row, col):
  delta_y, delta_x = delta
  new_row = row + delta_y
  new_col = col + delta_x
  valid_row = new_row >= 0 and new_row < len(grid)
  valid_col = new_col >= 0 and new_col < len(grid[0])
  return [[new_row, new_col], valid_row and valid_col]

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 1
grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["L", "L", "W", "W", "L"],
  ["W", "L", "W", "W", "L"],
  ["W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 2
grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "L", "W"],
  ["L", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 3
grid = [
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "L", "W", "W"],
  ["W", "W", "W", "W", "L", "L", "W", "W"],
  ["W", "W", "W", "W", "L", "L", "L", "W"],
  ["W", "W", "W", "W", "W", "L", "L", "L"],
  ["L", "W", "W", "W", "W", "L", "L", "L"],
  ["L", "L", "L", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 3
grid = [
  ["L", "L", "L", "L", "L", "L", "L", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "L", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "W", "W", "W", "W", "W", "W", "L"],
  ["L", "L", "L", "L", "L", "L", "L", "L"],
]
print(best_bridge(grid)) # -> 2
grid = [
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W", "W", "W", "L"],
]
print(best_bridge(grid)) # -> 8