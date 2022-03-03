def semesters_required(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)
  semesters = 0
  for course in graph:
    length = longest_education(graph, course)
    semesters = max(length, semesters)
  print(semesters)

def build_graph(num_courses, prereqs):
  graph = {}
  for num in range(num_courses):
    graph[num] = []
  for pair in prereqs:
    prereq, course = pair
    graph[prereq].append(course)
  return graph

def longest_education(graph, course):
  if not graph[course]:
    return 1
  res = 0
  for next_course in graph[course]:
    length = 1 + longest_education(graph, next_course)
    res = max(res, length)
  return res

# test_00:
num_courses = 6
prereqs = [
  [1, 2],
  [2, 4],
  [3, 5],
  [0, 5],
]
semesters_required(num_courses, prereqs) # -> 3
# test_01:
num_courses = 7
prereqs = [
  [4, 3],
  [3, 2],
  [2, 1],
  [1, 0],
  [5, 2],
  [5, 6],
]
semesters_required(num_courses, prereqs) # -> 5
# test_02:
num_courses = 5
prereqs = [
  [1, 0],
  [3, 4],
  [1, 2],
  [3, 2],
]
semesters_required(num_courses, prereqs) # -> 2
# test_03:
num_courses = 12
prereqs = []
semesters_required(num_courses, prereqs) # -> 1
# test_04:
num_courses = 3
prereqs = [
  [0, 2],
  [0, 1],
  [1, 2],
]
semesters_required(num_courses, prereqs) # -> 3
# test_05:
num_courses = 6
prereqs = [
  [3, 4],
  [3, 0],
  [3, 1],
  [3, 2],
  [3, 5],
]
semesters_required(num_courses, prereqs) # -> 2