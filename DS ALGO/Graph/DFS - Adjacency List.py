###### GRAPH IMPLEMENTATION ########

## DFS - Depth first Search (Adjacency List)

visited = {}
graph  = {}
def dfs(node):
    global visited
    global graph

    visited[node] = True
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)


def addedge(u,v):
    global graph

    if u not in graph:
        graph[u] = list()
    if v not in graph:
        graph[v] = list()

    graph[u].append(v)
    graph[v].append(u)


if __name__ == "__main__":
    addedge(1,2)
    addedge(2,3)
    addedge(2,4)
    addedge(4,5)
    addedge(5,1)
    addedge(4,4)
    dfs(1)


