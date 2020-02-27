"""
Dijkstra algorithm for search in graphs

Used to calculate the shortest distance between to nodes in a graph. 
When used with backtracking techniques, is also useful as a pathfinder algorithm (guarantees the shortest path)
If all edge weights are 1, works exactly like the bfs algorithm
"""

import heapq

graph = {
    0: {1: 1, 2: 3},
    1: {0: 1, 2: 3, 5: 2},
    2: {0: 3, 1: 3, 3: 3},
    3: {2: 3, 4: 5},
    4: {3: 5, 5: 1, 6: 2},
    5: {1: 2, 4: 1, 6: 3},
    6: {4: 2, 5: 3},
    7: {},
}


def find_shortest_path_between(graph, start_node, target_node):
    distance_to = [float('inf') for _ in range(len(graph))]
    distance_to[start_node] = 0

    shortest_path_to = [None for _ in range(len(graph))]
    processed = set()

    heap = []
    heapq.heappush(
        heap, (distance_to[start_node], start_node)
    )

    def dijkstra(node):
        while heap:
            distance, current_node = heapq.heappop(heap)

            for neighbor in graph[current_node]:
                if neighbor not in processed:
                    current_distance = distance_to[neighbor]
                    calculated_distance = distance_to[current_node] + \
                        graph[current_node][neighbor]

                    if current_distance > calculated_distance:
                        distance_to[neighbor] = calculated_distance
                        shortest_path_to[neighbor] = current_node

                    heapq.heappush(
                        heap, (distance_to[neighbor], neighbor)
                    )
            processed.add(current_node)

    dijkstra(start_node)

    path_stack = []
    current_node = target_node
    path_stack.append(current_node)

    while (current_node != start_node) and (current_node != None):
        current_node = shortest_path_to[current_node]
        path_stack.append(current_node)

    return (path_stack[::-1], distance_to[target_node])


if __name__ == "__main__":
    path, distance = find_shortest_path_between(graph, 0, 4)
    print(f'Shortest path from 0 to 4: {" -> ".join(map(str, path))}')
    print(f'Distance: {distance}')
