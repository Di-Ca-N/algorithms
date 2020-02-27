"""
Depth First Search algorithm for search in graphs.

Used to find connected components, search for some node (specially useful in a tree) or 
pathfinder (not very efficient and doesn't guarantee the shortest path) 

Graph used as example:
    0-1-5-6
    |/  |/
    2-3-4 7
"""

# in example, graph stored as adjacency list (but works with adjacency matrix as well with little changes)
# Example:
graph = {
    0: [1, 2],
    1: [0, 2, 5],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3, 5, 6],
    5: [1, 4, 6],
    6: [4, 5],
    7: [],
}


def find_connected_vertices_to(graph, vertice):
    """Given a graph and a vertice, find all other vertices that are connected to it"""

    visited = []  # if the visitation order to vertices isn't relevant, a set is better for performance purposes

    def dfs(node):
        """Actual DFS algorithm"""
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(vertice)

    return visited


if __name__ == "__main__":
    print(find_connected_vertices_to(graph, 0))
    print(find_connected_vertices_to(graph, 7))
