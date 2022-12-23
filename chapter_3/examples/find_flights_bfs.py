# finds flights by bfs

from shared.data_structured.tree import Node


def search_solution_by_bfs(connections, initial_state, solution):
    is_success = False
    visited_nodes = []
    border_nodes = []
    initial_node = Node(initial_state)
    border_nodes.append(initial_node)

    while (not is_success) and len(border_nodes) != 0:
        node = border_nodes[0]

        # extract node and append to visited
        visited_nodes.append(border_nodes.pop(0))
        if node.get_data() == solution:
            is_success = True
            return node

        # expand child node (cities with connections)
        data_node = node.get_data()
        children_list = []
        for a_child in connections[data_node]:
            child = Node(a_child)
            children_list.append(child)
            validate(child, visited_nodes, border_nodes)
            node.set_children(children_list)


def validate(node_child, visited_nodes, border_nodes):
    if not node_child.in_list(visited_nodes) and not node_child.in_list(border_nodes):
        border_nodes.append(node_child)


def init():
    connections = {
        'Malaga': {
            'Salamanca',
            'Madrid',
            'Barcelona'
        },
        'Sevilla': {
            'Santiago',
            'Madrid',
        },
        'Granada': {
            'Valencia'
        },
        'Madrid': {
            'Salamanca',
            'Sevilla',
            'Malaga',
            'Barcelona',
            'Santander',
        },
        'Salamanca': {
            'Malaga',
            'Madrid',
        },
        'Santiago': {
            'Sevilla',
            'Santander',
            'Barcelona',
        },
        'Santander': {
            'Santiago',
            'Madrid'
        },
        'Zaragoza': {
            'Barcelona'
        },
        'Barcelona': {
            'Zaragoza',
            'Santiago',
            'Madrid',
            'Malaga',
            'Valencia'
        }
    }
    initial_state = 'Malaga'
    solution = 'Santiago'
    solution_node = search_solution_by_bfs(connections, initial_state, solution)
    result = []
    node = solution_node
    while node.get_parent() is not None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print(result)

init()
