# traveling by road with A* search

from shared.data_structured.tree import Node
from math import sin, cos, acos

# constants
coord = {
    'Malaga': (36.43, -4.24),
    'Sevilla': (37.23, -5.59),
    'Granada': (37.11, -3.35),
    'Valencia': (39.28, -0.22),
    'Madrid': (40.24, -3.41),
    'Salamanca': (40.57, -5.40),
    'Santiago': (42.52, -8.33),
    'Santander': (43.28, -3.48),
    'Zaragoza': (41.39, -0.52),
    'Barcelona': (41.23, 2.11),
}
solution = 'Santiago'


def compare(x):
    # g(n) + h(n) to city x
    lat1 = coord[x.get_data()][0]
    lon1 = coord[x.get_data()][1]

    lat2 = coord[solution][0]
    lon2 = coord[solution][1]

    d = int(geodist(lat1, lon1, lat2, lon2))
    c1 = x.get_weight() + d

    # g(n) + h(n) to city y
    # lat1 = coord[y.get_data()][0]
    # lon1 = coord[y.get_data()][1]
    #
    # lat2 = coord[solution][0]
    # lon2 = coord[solution][1]
    #
    # d = int(geodist(lat1, lon1, lat2, lon2))
    # c2 = y.get_weight() + d

    # return c1 - c2
    return c1


def geodist(lat1, lon1, lat2, lon2):
    """
    calculate the geodistance between two coordinates
    """
    grad_rad = 0.01745329
    rad_grad = 57.29577951
    longitude = lon1-lon2
    val = (
        sin(lat1 * grad_rad) * sin(lat2 * grad_rad)
    ) + (
        cos(lat1 * grad_rad) * cos(lat2 * grad_rad) * cos(longitude * grad_rad)
    )
    return (acos(val) * rad_grad) * 111.32


def search_solution_by_UCS(connections, initial_state, solution):
    is_success = False
    visited_nodes = []
    border_nodes = []
    initial_node = Node(initial_state)
    initial_node.set_weight(0)
    border_nodes.append(initial_node)
    while(not is_success) and len(border_nodes) != 0:
        # sorted border nodes list
        border_nodes = sorted(border_nodes, key=compare)
        node = border_nodes[0]

        # extract node and append to visited nodes list
        visited_nodes.append(border_nodes.pop(0))
        if node.get_data() == solution:
            # solution was found
            is_success = True
            return node
        # expand  children nodes (cities with connections)
        data_node = node.get_data()
        children_list = []
        for a_child in connections[data_node]:
            child = Node(a_child)
            # calculate g(n): cumulative cost
            cost = connections[data_node][a_child]
            child.set_weight(node.get_weight() + cost)
            children_list.append(child)
            if not child.in_list(visited_nodes):
                # if it is in this list we are going to interchange with
                # the new cost value if is less
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
    solution_node = search_solution_by_UCS(connections, initial_state, solution)

    # show result
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




