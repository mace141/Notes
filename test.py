from collections import deque

def closest_carrot(grid, row, col):
  visited = set()
  deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  queue = deque([[row, col, 0]])
  while queue:
    r, c, dst = queue.popleft()
    visited.add((r, c))
    if grid[r][c] == 'C':
      return dst
    for delta in deltas:
      delta_y, delta_x = delta
      new_row = r + delta_y
      new_col = c + delta_x
      valid_row = new_row >= 0 and new_row < len(grid)
      valid_col = new_col >= 0 and new_col < len(grid[0])
      valid_pos = valid_row and valid_col
      visited_pos = (new_row, new_col) in visited
      if valid_pos and grid[new_row][new_col] != 'X' and not visited_pos:
        queue.append([new_row, new_col, dst + 1])

  return -1

# test_00:
grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]
print(closest_carrot(grid, 1, 2)) # -> 4
# test_01:
grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]
print(closest_carrot(grid, 0, 0)) # -> 5
# test_02:
grid = [
  ['O', 'O', 'X', 'X', 'X'],
  ['O', 'X', 'X', 'X', 'C'],
  ['O', 'X', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'C', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O'],
]
print(closest_carrot(grid, 3, 4)) # -> 9
# test_03:
grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
]

print(closest_carrot(grid, 1, 4)) # -> 2
# test_04:
grid = [
  ['O', 'O', 'X', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['O', 'X', 'C', 'C', 'O'],
]
print(closest_carrot(grid, 2, 0)) # -> -1
