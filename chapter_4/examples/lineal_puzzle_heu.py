# Lineal puzzle using heuristic function
from shared.data_structured.tree import Node


def search_solution_with_heuristic(initial_node, solution, visited):
    visited.append(initial_node.get_data())
    if initial_node.get_data() == solution:
        return initial_node
    # expand to successors nodes
    data_node = initial_node.get_data()
    child = [
        data_node[1],
        data_node[0],
        data_node[2],
        data_node[3],
    ]
    left_child = Node(child)

    child = [
        data_node[0],
        data_node[2],
        data_node[1],
        data_node[3],
    ]
    central_child = Node(child)

    child = [
        data_node[0],
        data_node[1],
        data_node[3],
        data_node[2],
    ]
    right_child = Node(child)

    initial_node.set_children([
        left_child,
        central_child,
        right_child
    ])

    for child_node in initial_node.get_children():
        if child_node.get_data() not in visited and improve(initial_node, child_node):
            # recursive call
            solution_node = search_solution_with_heuristic(
                child_node, solution, visited
            )
            if solution_node is not None:
                return solution_node
    return None


def improve(parent_node, child_node):
    parent_quality = 0
    child_quality = 0
    parent_data = parent_node.get_data()
    child_data = child_node.get_data()

    for n in range(1, len(parent_data)):
        if parent_data[n] > parent_data[n-1]:
            parent_quality += 1
        if child_data[n] > child_data[n - 1]:
            child_quality += 1

    return child_quality >= parent_quality


def init():
    initial_state = [4, 2, 3, 1]
    solution = [1, 2, 3, 4]
    visited = []
    initial_node = Node(initial_state)
    node = search_solution_with_heuristic(initial_node, solution, visited)

    # show result
    result = []
    while node.get_parent() is not None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print(result)


init()
