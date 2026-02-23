def graph_coloring(graph: list[list[int]], m: int):
    colors = [-1] * len(graph)
    
    
    def is_safe(v: int, c: int):
        for i in graph[v]:
            if colors[i] == c:
                return False
        return True
    
    
    def color_graph(v: int):
        if v == len(graph):
            return True

        for c in range(m):
            if is_safe(v, c):
                colors[v] = c

                if color_graph(v + 1):
                    return True

                colors[v] = -1

        return False
    
    return color_graph(0), colors


graph = [[1, 2], [0, 2], [0, 1]]
m = 3
result, coloring = graph_coloring(graph, m)

print(result, coloring)
