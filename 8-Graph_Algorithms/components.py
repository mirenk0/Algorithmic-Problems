def dfs(graph, visited, i):
    visited[i] = True
    for neighbor in graph[i]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def count_components(N):
    graph = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        for j in range(i, N + 1, i):
            graph[i].append(j)
            graph[j].append(i)

    visited = [False] * (N + 1)
    count = 0
    for i in range(2, N + 1):
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1
    return count


if __name__ == "__main__":
    N = 1000
    print(count_components(N))
