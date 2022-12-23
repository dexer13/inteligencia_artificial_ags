# TSP with simulated annealing
import math
import random

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


def distance(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]

    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2)**2)


# calculate distance over a route
def check_route(route):
    total = 0
    for i in range(0, len(route) - 1):
        city_1 = route[i]
        city_2 = route[i+1]
        total += distance(coord[city_1], coord[city_2])
    city_1 = route[i+1]
    city_2 = route[0]
    total += distance(coord[city_1], coord[city_2])
    return total


def simulated_annealing(route):
    T = 20
    T_MIN = 0
    v_refreshing = 100

    while T>T_MIN:
        current_dist = check_route(route)
        for i in range(1, v_refreshing):
            # random swap two cities
            i = random.randint(0, len(route) - 1)
            j = random.randint(0, len(route) - 1)
            route_tmp = route[:]
            city_temp = route_tmp[i]
            route_tmp[i] = route_tmp[j]
            route_tmp[j] = city_temp
            dist = check_route(route_tmp)
            delta = current_dist - dist
            if dist < current_dist:
                route = route_tmp[:]
                break
            if random.random() < math.exp(delta/T):
                route = route_tmp[:]
                break
        # refreshing T linearly
        T -= 0.005
    return route


def main():
    # create initial route
    route = []
    for city in coord:
        route.append(city)
    random.shuffle(route)

    route = simulated_annealing(route)
    print(route)
    print(f'Total distance: {check_route(route)}')


main()
