"""
Breadth First Search algorithm for search in graphs.

Used to find connected components, search for some node or pathfinder (as efficient as Djikstra if all edges has weight 1. In this case, guarantees the shortest path) 

Graph used as example:
    0-1-5-6
    |/  |/
    2-3-4 7
"""

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
    visited = []  # if the visitation order to vertices isn't relevant, a set is better for performance purposes

    def bfs(node):
        """Actual BFS algorithm"""
        queue = []
        queue.append(vertice)

        while queue:
            current_vertice = queue.pop(0)

            if current_vertice not in visited:
                visited.append(current_vertice)

                for neighbor in graph[current_vertice]:
                    queue.append(neighbor)

    bfs(vertice)
    return visited


if __name__ == "__main__":
    print(find_connected_vertices_to(graph, 0))
    print(find_connected_vertices_to(graph, 7))
