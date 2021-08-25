def semesters_required(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  semesters = 1
  for course in graph:
    length = longest_path(graph, course)
    semesters = length if length > semesters else semesters
  return semesters

def build_graph(num_courses, prereqs):
  graph = {}
  for num in range(num_courses):
    graph[num] = []
  for pair in prereqs:
    prereq, course = pair
    graph[prereq].append(course)
  return graph

def longest_path(graph, course):
  if not graph[course]:
    return 1
  max = 0
  for next_course in graph[course]:
    length = longest_path(graph, next_course)
    max = length if length > max else max
  return 1 + max

num_courses = 6
prereqs = [
  [1, 2],
  [2, 4],
  [3, 5],
  [0, 5],
]
print(semesters_required(num_courses, prereqs)) # -> 3
num_courses = 7
prereqs = [
  [4, 3],
  [3, 2],
  [2, 1],
  [1, 0],
  [5, 2],
  [5, 6],
]
print(semesters_required(num_courses, prereqs)) # -> 5
num_courses = 5
prereqs = [
  [1, 0],
  [3, 4],
  [1, 2],
  [3, 2],
]
print(semesters_required(num_courses, prereqs)) # -> 2
num_courses = 12
prereqs = []
print(semesters_required(num_courses, prereqs)) # -> 1
num_courses = 3
prereqs = [
  [0, 2],
  [0, 1],
  [1, 2],
]
print(semesters_required(num_courses, prereqs)) # -> 3
num_courses = 6
prereqs = [
  [3, 4],
  [3, 0],
  [3, 1],
  [3, 2],
  [3, 5],
]
print(semesters_required(num_courses, prereqs)) # -> 2