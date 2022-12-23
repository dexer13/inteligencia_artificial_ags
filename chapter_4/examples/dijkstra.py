import sys


def dijkstra(graph, initial_node):
    tags = {}
    visited = []
    pending = [initial_node]
    current_node = initial_node

    # initial node
    tags[current_node] = [0, '']
    # let select the next node with less acumulated heavy
    while len(pending) > 0:
        current_node = get_least_weight_node(tags, visited)
        visited.append(current_node)

        # get adjacent nodes
        for adjacent, weight in graph[current_node].items():
            if adjacent not in pending and adjacent not in visited:
                pending.append(adjacent)
            new_weight = tags[current_node][0] + graph[current_node][adjacent]
            # label
            if adjacent not in visited:
                if adjacent not in tags:
                    tags[adjacent] = [new_weight, current_node]
                else:
                    if tags[adjacent][0] > new_weight:
                        tags[adjacent] = [new_weight, current_node]
        del pending[pending.index(current_node)]
    return tags


def get_least_weight_node(tags, visited):
    smaller = float('inf')
    for node, tags in tags.items():
        if tags[0] < smaller and node not in visited:
            smaller = tags[0]
            smaller_node = node
    return smaller_node


def main():
    graph = {
        '1': {'3': 6, '2': 3},
        '2': {'4': 1, '1': 3, '3': 2},
        '3': {'1': 6, '2': 2, '4': 4, '5': 2},
        '4': {'2': 1, '3': 4, '5': 6},
        '5': {'3': 2, '4': 6, '6': 2, '7': 2},
        '6': {'5': 2, '7': 3},
        '7': {'5': 2, '6': 3},
    }
    tags = dijkstra(graph, '1')
    print(tags)


main()