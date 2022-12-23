# VRP
import math
from operator import itemgetter

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
orders = {
    'Malaga': 10,
    'Sevilla': 13,
    'Granada': 7,
    'Valencia': 11,
    'Madrid': 15,
    'Salamanca': 8,
    'Santiago': 6,
    'Santander': 7,
    'Zaragoza': 8,
    'Barcelona': 14
}

storage = (40.23, -3.40)
max_charge = 40


def distance(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]

    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2)**2)


def in_route(routes, c):
    route = None
    for r in routes:
        if c in r:
            route = r
    return route


def weight_route(route):
    total = 0
    for c in route:
        total += orders[c]
    return total

def vrp_greedy():
    # calculate saving
    s = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2:
                if not (c2, c1) in s:
                    d_c1_c2 = distance(coord[c1], coord[c2])
                    d_c1_storage = distance(coord[c1], storage)
                    d_c2_storage = distance(coord[c2], storage)
                    s[c1, c2] = d_c1_storage + d_c2_storage - d_c1_c2

    # sort savings
    s = sorted(s.items(), key=itemgetter(1), reverse=True)

    # build routes
    routes = []
    for k, v in s:
        rc1 = in_route(routes, k[0])
        rc2 = in_route(routes, k[1])
        if rc1 is None and rc2 is None:
            # aren't in any route. let create
            if weight_route([k[0], k[1]]) <= max_charge:
                routes.append([k[0], k[1]])
        elif rc1 is not None and rc2 is None:
            # city 1 already is in a route. Append the city
            if rc1[0] == k[0]:
                if weight_route(rc1) + weight_route([k[1]]) <= max_charge:
                    routes[routes.index(rc1)].insert(0, k[1])
            elif rc1[len(rc1) - 1] == k[0]:
                if weight_route(rc1) + weight_route([k[1]]) <= max_charge:
                    routes[routes.index(rc1)].append(k[1])
        elif rc1 is None and rc2 is not None:
            # city 2 already is in a route. Append the city
            if rc2[0] == k[1]:
                if weight_route(rc2) + weight_route([k[0]]) <= max_charge:
                    routes[routes.index(rc2)].insert(0, k[0])
            elif rc2[len(rc2) - 1] == k[1]:
                if weight_route(rc2) + weight_route([k[0]]) <= max_charge:
                    routes[routes.index(rc2)].append(k[0])
        elif rc1 is not None and rc2 is not None and rc1 != rc2:
            # city 1 and 2 already are in route. let treat join them
            if rc1[0] == k[0] and rc2[len(rc2)-1] == k[1]:
                if weight_route(rc1) + weight_route(rc2) <= max_charge:
                    routes[routes.index(rc2)].extend(rc1)
                    routes.remove(rc1)
            elif rc1[len(rc1)-1] == k[0] and rc2[0] == k[1]:
                if weight_route(rc1) + weight_route(rc2) <= max_charge:
                    routes[routes.index(rc1)].extend(rc2)
                    routes.remove(rc2)
    return routes


def main():
    routes = vrp_greedy()
    for route in routes:
        print(route)


main()
