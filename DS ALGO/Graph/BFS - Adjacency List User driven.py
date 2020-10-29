### BFS - Adjacency List  -User driven

visited = dict()
graph = dict()

def add_edge(a,b):
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
    
    graph[a].append(b)
    graph[b].append(a)

def Bfs(node):
    queue = []
    queue.append(node)
    visited[node] = True

    while len(queue) > 0:
        x = queue.pop(0)
        print(x)

        for neighbor in graph[x]:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
               

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