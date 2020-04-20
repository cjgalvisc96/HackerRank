from Graph import Graph


def find_all_paths(self, start_vertex, end_vertex, path=[]):
    """ find all paths from start_vertex to 
            end_vertex in graph """
    graph = self.__graph_dict
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = self.find_all_paths(vertex, end_vertex, path)
            for p in extended_paths:
                paths.append(p)
    return paths


if __name__ == "__main__":
    g = {
        "a": ["d", "f"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": ["d"],
    }
    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('All paths from vertex "a" to vertex "b":')
    path = graph.find_all_paths("a", "b")
    print(path)

    print('All paths from vertex "a" to vertex "f":')
    path = graph.find_all_paths("a", "f")
    print(path)

    print('All paths from vertex "c" to vertex "c":')
    path = graph.find_all_paths("c", "c")
    print(path)
