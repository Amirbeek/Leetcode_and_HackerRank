def countServers( grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    pos = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                pos.append((x,y))


    return pos

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
arr = [[1,1,0,0],
       [0,0,1,0],
       [0,0,1,0],
       [0,0,0,1]]
print(countServers(arr))
