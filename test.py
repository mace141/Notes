import pdb
pdb.set_trace()

def exist(board, word):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if search(board, i, j, word, 0, set()):
        return True

  return False

def search(board, r, c, word, i, visited):
  if i == len(word):
    return True
  if (r, c) in visited:
    return False
  if r == len(board) or c == len(board[0]):
    return False
  if r < 0 or c < 0:
    return False
  
  if board[r][c] == word[i]:
    visited.add((r, c))
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dy, dx in deltas:
      if search(board, r + dy, c + dx, word, i + 1, visited):
        return True
    visited.remove((r, c))

  return False

board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCEFSADEESE"
print(exist(board, word))