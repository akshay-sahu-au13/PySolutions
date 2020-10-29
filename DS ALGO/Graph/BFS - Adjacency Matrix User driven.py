## BFS - Using Adjacency Matrix

graph = [[0 for i in range(100)] for j in range(100)]
visited = dict()

def add_edge(a,b):
    graph[a][b] = 1
    graph[b][a] = 1

def Bfs(node):
    queue = []
    queue.append(node)
    visited[node] = True

    while len(queue) > 0:
        x = queue.pop(0)
        print(x)

        for col in range(len(graph[0])):
            if graph[x][col] == 1:
                if col not in visited:
                    visited[col] = True
                    queue.append(col)

if __name__ == "__main__":

    while True:
        Input = input("Enter 1 to add edges or X to quit: ")
        if Input == "1":
            a = int(input("Enter value of a: "))
            b = int(input("Enter value of b: "))
            add_edge(a,b)
        elif Input.lower() == "x":
            break
        else:
            print("Enter a valid input")

    Bfs(int(input("Enter any one of the vertex: ")))