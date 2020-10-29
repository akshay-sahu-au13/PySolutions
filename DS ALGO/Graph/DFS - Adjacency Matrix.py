
## DFS - Depth First Search (Adjacency Matrix)

graph = [[0 for i in range(100)] for j in range(100)]
visited = {}

def addedge(u,v):
    global graph

    graph[u][v] = 1
    graph[v][u] = 1

def dfs(node):
    global graph
    global visited

    visited[node] = True
    print(node)

    for col in range(len(graph[0])):
        if graph[node][col] == 1:
            if col not in visited:
                dfs(col)
        
if __name__ == "__main__":
    addedge(1,2)
    addedge(2,3)
    addedge(2,4)
    addedge(4,5)
    addedge(5,1)
    addedge(4,4)
    dfs(1)
