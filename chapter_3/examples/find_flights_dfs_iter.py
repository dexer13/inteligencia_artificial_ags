# find flights using dfs iterative

from shared.data_structured.tree import Node


def dfs_prof_iter(connections, node, solution):
    for limit in range(0, 1000):
        visited = []
        solution_found = search_solution_dfs_rec(connections, node, solution, visited, limit)
        if solution_found is not None:
            return solution_found


def search_solution_dfs_rec(connections, node, solution, visited, limit):
    if limit > 0:
        visited.append(node)
        if node.get_data() == solution:
            return node
        # expand children nodes (cities with connections)
        node_data = node.get_data()
        list_children = []
        for a_child in connections[node_data]:
            child = Node(a_child)
            if not child.in_list(visited):
                list_children.append(child)
        node.set_children(list_children)

        for child_node in node.get_children():
            if child_node not in visited:
                # recursive call
                solution_found = search_solution_dfs_rec(connections, child_node, solution, visited, limit-1)
                if solution_found is not None:
                    return solution_found
        return None


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
        },
        'Valencia': {'Barcelona'}
    }
    initial_state = 'Malaga'
    solution = 'Santiago'
    initial_node = Node(initial_state)
    solution_node = dfs_prof_iter(connections, initial_node, solution)
    result = []
    node = solution_node
    if node is not None:
        while node.get_parent() is not None:
            result.append(node.get_data())
            node = node.get_parent()
        result.append(initial_state)
        result.reverse()
        print(result)
    else:
        print('solution is not found')


init()
