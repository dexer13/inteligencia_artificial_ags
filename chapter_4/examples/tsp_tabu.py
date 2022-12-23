# TSP with tabu searching

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


def tabu_searching(route):
    best_route = route
    tabu_memory = {}
    persistence = 5
    improving = False
    iterations = 100

    while iterations > 0:
        iterations = iterations - 1
        current_dist = check_route(route)
        # check neighbors
        improving = False
        for i in range(0, len(route)):
            if improving:
                break
            for j in range(0, len(route)):
                if i != j:
                    tmp_route = route[:]
                    tmp_city = tmp_route[i]
                    tmp_route[i] = tmp_route[j]
                    tmp_route[j] = tmp_city
                    dist = check_route(tmp_route)

                    # check if the movement is tabu
                    tabu = False
                    key = f'{tmp_route[i]}_{tmp_route[j]}'
                    if key in tabu_memory:
                        if tabu_memory[key] > 0:
                            tabu = True

                    key = f'{tmp_route[j]}_{tmp_route[i]}'
                    if key in tabu_memory:
                        if tabu_memory[key] > 0:
                            tabu = True
                    if dist < current_dist and not tabu:
                        #find neighbors to improve the result
                        route = tmp_route[:]
                        if check_route(route) < check_route(best_route):
                            best_route = route[:]
                        # stage in tabu memory
                        tabu_memory[f'{tmp_route[i]}_{tmp_route[j]}'] = persistence
                        improving = True
                        break
                    elif dist < current_dist and tabu:
                        # check the acceptance requirement
                        # even if is a tabu movement
                        if check_route(tmp_route) < check_route(best_route):
                            best_route = tmp_route[:]
                            route = tmp_route[:]
                            # storage in tabu
                            tabu_memory[f'{tmp_route[i]}_{tmp_route[j]}'] = persistence
                            improving = True
                            break
        if len(tabu_memory) > 0:
            for k in tabu_memory.keys():
                if tabu_memory[k] > 0:
                    tabu_memory[k] = tabu_memory[k] -1
    return best_route


def main():
    # create initial route
    route = [city for city in coord.keys()]
    random.shuffle(route)

    route = tabu_searching(route)
    print(route)
    print(f'Total distance: {check_route(route)}')

main()