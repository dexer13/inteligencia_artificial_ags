# Lineal puzzle with Breadth First Search (BFS)

from shared.data_structured.tree import Node


def search_with_bfs_solution(initial_state, solution):
    is_success = False
    visited_nodes = []
    border_nodes = []
    initial_node = Node(initial_state)
    border_nodes.append(initial_node)
    while(not is_success) and len(border_nodes) != 0:
        node = border_nodes.pop(0)
        # extract node and append to visited nodes
        visited_nodes.append(node)
        if node.get_data() == solution:
            # solution was found
            is_success = True
            return node
        # expand to children node
        data_node = node.get_data()
        # left operator 2134 -> [12]34
        children = [
            data_node[1],
            data_node[0],
            data_node[2],
            data_node[3],
        ]
        left_child = Node(children)
        validate(left_child, visited_nodes, border_nodes)

        # central operator 1324 -> 1[23]4
        child = [
            data_node[0],
            data_node[2],
            data_node[1],
            data_node[3],
        ]
        central_child = Node(child)
        validate(central_child, visited_nodes, border_nodes)

        # right operator 1243 -> 12[34]
        child = [
            data_node[0],
            data_node[1],
            data_node[3],
            data_node[2]
        ]
        right_child = Node(child)
        validate(right_child, visited_nodes, border_nodes)
        node.set_children([left_child, central_child, right_child])


def validate(node_child, visited_nodes, border_nodes):
    if not node_child.in_list(visited_nodes) and not node_child.in_list(border_nodes):
        border_nodes.append(node_child)


def init():
    initial_state = [4, 2, 3, 1]
    solution = [1, 2, 3, 4]
    solution_node = search_with_bfs_solution(initial_state, solution)
    # show result
    result = []
    node = solution_node
    while node.get_parent() is not None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print(result)

init()
