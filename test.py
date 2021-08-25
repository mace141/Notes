def longest_path(graph):
  longest = float('-inf')
  for node in graph:
    length = traverse(graph, node)
    longest = length if longest < length else longest
  return longest

def traverse(graph, node):
  if not graph[node]:
    return 0
  max = 0
  for neighbor in graph[node]:
    length = traverse(graph, neighbor)
    max = max if max > length else length
  return 1 + max

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}
print(longest_path(graph)) # -> 2
graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}
print(longest_path(graph)) # -> 4
graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}
print(longest_path(graph)) # -> 2
graph = {
  'a': ['b'],
  'b': ['c'],
  'c': [],
  'e': ['f'],
  'f': ['g'],
  'g': ['h'],
  'h': []
}
print(longest_path(graph)) # -> 3