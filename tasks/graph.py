class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def point_to(self, node):
        self.children.append(node)


class Graph:
    def __init__(self, root):
        self.root = root

    def dfs(self):
        visited = []

        def traverse(node):
            visited.append(node)

            for child in node.children:
                if child not in visited:
                    traverse(child)

        traverse(self.root)

        return visited

    def bfs(self):
        visited = []
        queue = [self.root]

        while queue:  # while queue is not empty 
            node = queue.pop()  # take the first element from the queue 
            visited.append(node)  # add it to the list of visited nodes 

            for child in node.children:  # add all children of the current node to the queue 
                if child not in visited and child not in queue:   # check if they were already added to the list of visited nodes or to the queue 
                    queue.insert(0, child)   # insert them at the beginning of the queue (FIFO) 

        return visited