# Directed graph
class Graph():

  def __init__(self):
    self.graph = {}

  def add(self, from_vertex, to_vertex):
    # Add edge
    if from_vertex in self.graph:
      self.graph[from_vertex].append(to_vertex)

    # Add vertex
    else:
      self.graph[from_vertex] = [to_vertex]

  def remove(self, vertex):
    if vertex in self.graph:
      print(vertex)
      del self.graph[vertex]
    for vertices in self.graph.values():
      print(self.graph.values())
      if vertex in vertices:
        vertices.remove(vertex)
  
  def display(self):
    for vertex in self.graph:
      adjacent_vertices = " ".join(map(str, self.graph[vertex]))
      print(f"{vertex} -> {adjacent_vertices}")

  def bfs(self, start_vertex):
    # Check if the start vertex exists in the graph
    if start_vertex not in self.graph:
      return [] # If not, return an empty list
    
    queue = [start_vertex] # Initialize a queue with start_vertex
    traversal = [] # Initialize an empty list to store the BFS traversal result

    while queue:  # Continue until queue is empty
      vertex = queue.pop(0) # Remove and retrieve the first vertex from the queue (FIFO)
      if vertex not in traversal: # Check of the vertex has not been visited
        traversal.append(vertex) # Add the vertex to the traversal result
        if vertex in self.grap: # Check if the vertex exists in the graph
          queue.extend(self.graph[vertex]) # Add all adjacent vertices to the current vertex to the queue

    return traversal # Return the BFS traversal result
  
  def dfs(self, start_vertex):
    # Check if the start_vertex exisits in the graph
    if start_vertex not in self.graph:
      return [] # If not, return an empty list
    
    stack = [start_vertex] # Initialize a stack with the start_vertex
    traversal = [] # Intialize an empty list to store the DFS traversal result

    while stack:  # Continue until the stack is empty
      vertex = stack.pop()  # Remove and retireve the last vertex from the stack (LIFO)
      if vertex not in traversal: # Check if the vertex has not been visited
        traversal.append(vertex)  # Add the vertex to the traversal result
        if vertex in self.graph:  # Check if the vertex exists in the graph
          stack.extend(reversed(self.graph[vertex]))   # Add all adjacent vertices of the current vertex to the stack

    return traversal


g = Graph()

g.add(1,2)
g.add(1,3)
g.add(2,1)
print(g.graph)
g.display()
g.remove(1)
print(g.graph)
