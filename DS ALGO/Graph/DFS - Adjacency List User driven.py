### DFS - Adjacency List -- User Driven

visited = {}
graph = {}

def add_edge(a,b):
    global graph

    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()

    graph[a].append(b)
    graph[b].append(a)

def Dfs(node):
    global graph
    global visited

    visited[node] = True
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            Dfs(neighbor)

if __name__ == "__main__":

    while True:
        Input = input("Enter 1 to add edges and X or x to quit:")
        if Input.lower() == "x":
            break
        elif Input == "1":
            vertex1 = int(input("Enter a: "))
            vertex2 = int(input("Enter b: "))
            add_edge(vertex1,vertex2)

        else:
            print("Invalid choice, please press 1 or X.")

    Dfs(int(input("Enter any of the vertex that you've already entered: ")))