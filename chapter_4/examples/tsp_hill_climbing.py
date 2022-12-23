# TSP with hill climbing

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


# calculate distance
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


def hill_climbing():
    # create random initial route
    route = []
    for city in coord:
        route.append(city)
    random.shuffle(route)

    improving = True
    while improving:
        improving = False
        current_distance = check_route(route)
        # evaluate neighbors
        for i in range(0, len(route)):
            if improving:
                break
            for j in range(0, len(route)):
                if i != j:
                    route_tmp = route[:]
                    city_tmp = route_tmp[i]
                    route_tmp[i] = route_tmp[j]
                    route_tmp[j] = city_tmp
                    dist = check_route(route_tmp)
                    if dist < current_distance:
                        # find neighbor which improve the result
                        improving = True
                        route = route_tmp[:]
                        break
    return route


def main():
    route = hill_climbing()
    print(route)
    print(f'Total distance: {check_route(route)}')


main()
