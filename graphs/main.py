from Graph import Graph

if __name__ == "__main__":
    granph_input = {
        "a": ["d", "f"],
        "b": ["c"],
        "c": ["b", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": ["d"],
    }
    graph = Graph(granph_input)
    vertices = graph.vertices()
    edges = graph.edges()
    print("*" * 15)
    print("Graph Info")
    print("*" * 15)

    print("*" * 15)
    print("All paths combinations")
    print("*" * 15)
    """
    for vertice_1 in vertices:
        for vertice_2 in vertices:
            if vertice_1 != vertice_2:
                print(f'All paths from vertex "{vertice_1}" to vertex "{vertice_2}":')
                print(f"{graph.find_all_paths(vertice_1, vertice_2)}\n")
    """
    print(graph.find_all_paths("a", "e"))

