# find the best route using uniform cost search (UCS)
from shared.data_structured.tree import Node


def search_solution_by_ucs(connections, initial_state, solution):
    is_success = False
    visited_nodes = []
    border_nodes = []
    initial_node = Node(initial_state)
    initial_node.set_weight(0)
    border_nodes.append(initial_node)

    while (not is_success) and len(border_nodes) != 0:
        # sort border nodes list by weight
        border_nodes = sorted(border_nodes, key=lambda x: x.get_weight())
        node = border_nodes[0]

        # extract nodes and append to visited nodes list
        visited_nodes.append(border_nodes.pop(0))
        if node.get_data() == solution:
            # solution found
            is_success = True
            return node
        # expand children nodes (cities with connections)
        data_node = node.get_data()
        children_list = []
        for a_child in connections[data_node]:
            child = Node(a_child)
            weight = connections[data_node][a_child]
            child.set_weight(node.get_weight() + weight)
            children_list.append(child)

            if not child.in_list(visited_nodes):
                # if this is in list and the value is less we replace with the new value
                if child.in_list(border_nodes):
                    for n in border_nodes:
                        if n.is_equal(child) and n.get_weight() > child.get_weight():
                            border_nodes.remove(n)
                            border_nodes.append(child)
                else:
                    border_nodes.append(child)
        node.set_children(children_list)


def init():
    connections = {
        'Malaga': {
            'Granada': 125,
            'Madrid': 513,
        },
        'Sevilla': {
            'Madrid': 514
        },
        'Granada': {
            'Malaga': 125,
            'Madrid': 423,
            'Valencia': 491,
        },
        'Valencia': {
            'Granada': 491,
            'Madrid': 356,
            'Zaragoza': 309,
            'Barcelona': 346,
        },
        'Madrid': {
            'Salamanca': 203,
            'Sevilla': 514,
            'Malaga': 513,
            'Granada': 423,
            'Barcelona': 603,
            'Santander': 437,
            'Valencia': 356,
            'Zaragoza': 313,
            'Santiago': 599,
        },
        'Salamanca': {
            'Santiago': 390,
            'Madrid': 203,
        },
        'Santiago': {
            'Salamanca': 390,
            'Madrid': 599,
        },
        'Santander': {
            'Madrid': 437,
            'Zaragoza': 394,
        },
        'Zaragoza': {
            'Barcelona': 296,
            'Valencia': 309,
            'Madrid': 313,
        },
        'Barcelona': {
            'Zaragoza': 296,
            'Madrid': 603,
            'Valencia': 349,
        },
    }
    initial_state = 'Malaga'
    solution = 'Santiago'
    solution_node = search_solution_by_ucs(connections, initial_state, solution)

    # show solution
    result = []
    node = solution_node
    while node.get_parent() is not None:
        result.append(node.get_data())
        node = node.get_parent()
    result.append(initial_state)
    result.reverse()
    print(result)
    print(f'coste: {solution_node.get_weight()}')


init()



