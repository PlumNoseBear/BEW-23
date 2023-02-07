from typing import Any
__all__ = (
    'Node',
    'Graph'
)


class Node:
  def __init__(self, name):
      self.name=name
      self.z, self.vertexes={},[]
      self.z[self.name]=self.vertexes

  def point_to(self, vertex_join):
      self.vertexes.append(vertex_join.name)
      self.z[self.name]=self.vertexes
      return self.z

class Graph:
  def __init__(self, root):
    self.root=root

  def dfs(self):
          r = self.root
          visited = []
          stack = []
                    
          visited.append(r.name)
          for value in a.z.values():
            res=value
          stack=stack+value
          print(visited,  stack)
          return
