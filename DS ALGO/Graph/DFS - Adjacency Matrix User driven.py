## DFS - Adjacency Matrix - User Driven

visited = dict()
graph = [[0 for x in range(100)]for x in range(100)]

def add_edge(x,y):
    global graph

    graph[x][y] = 1
    graph[y][x] = 1

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

    dfs(int(input("Enter any of the vertex that you've already entered: ")))