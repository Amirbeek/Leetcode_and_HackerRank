graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

class Graph:
    def __init__(self):  # fixed typo: __int__ ➝ __init__
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList[node] = []
            self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        # Check if both nodes exist
        if node1 not in self.adjacentList or node2 not in self.adjacentList:
            return "Please add both vertices first."
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnection(self):
        for node in self.adjacentList:
            connections = " ".join(str(neighbor) for neighbor in self.adjacentList[node])
            print(f"{node} --> {connections}")


# Test the Graph
g = Graph()

# Add vertices
for edge in graph:
    g.addVertex(edge[0])
    g.addVertex(edge[1])

# Add edges
for edge in graph:
    g.addEdge(edge[0], edge[1])

# Show connections
g.showConnection()
