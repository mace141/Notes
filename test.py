def has_cycle(graph):
  visited = set()
  for node in graph:
    if in_cycle(graph, node, visited, set()):
      return True
  return False

def in_cycle(graph, node, visited, visiting):
  if node in visited:
    return False
  if node in visiting:
    return True

  visiting.add(node)
  for neighbor in graph[node]:
    if in_cycle(graph, neighbor, visited, visiting):
      return True
  visiting.remove(node)
  visited.add(node)
  
  return False

print(has_cycle({
  'a': ["b"],
  'b': ["c"],
  'c': ["a"],
})) # -> true
print(has_cycle({
  'a': ["b", "c"],
  'b': ["c"],
  'c': ["d"],
  'd': [],
})) # -> false
print(has_cycle({
  'a': ["b", "c"],
  'b': [],
  'c': [],
  'e': ["f"],
  'f': ["e"],
})) # -> true
print(has_cycle({
  'q': ["r", "s"],
  'r': ["t", "u"],
  's': [],
  't': [],
  'u': [],
  'v': ["w"],
  'w': [],
  'x': ["w"],
})) # -> false
print(has_cycle({
  'a': ["b"],
  'b': ["c"],
  'c': ["a"],
  'g': [],
})) # -> true