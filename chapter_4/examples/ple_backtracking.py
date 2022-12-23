# PLE with backtracking

def backtracking(variables, variables_range, optimum, deep):
    min = variables_range[deep][0]
    max = variables_range[deep][1]

    for v in range(min, max):
        variables[deep] = v
        if deep < len(variables) - 1:
            # Can be completed if it does not meet any condition
            if is_completable(variables):
                optimum = backtracking(variables[:], variables_range, optimum, deep+1)
        else:
            # we are in a leave. let check solution
            solution = calculate_solution(variables)
            if solution > calculate_solution(optimum) and is_completable(variables):
                optimum = (variables[0], variables[1])
    return optimum


def calculate_solution(variables):
    x1 = variables[0]
    x2 = variables[1]
    val = (12-6) * x1 + (8-4) * x2
    return val


def is_completable(variables):
    x1 = variables[0]
    x2 = variables[1]
    val1 = 7 * x1 + 4 * x2
    val2 = 6 * x1 + 5 * x2
    return val1 <= 150 and val2 <= 160


def init():
    # values to variables x1 and x2
    variables = [0, 0]
    # range of variables x1 and x2
    variables_range = [(0, 51), (0, 76)]
    # best solution found
    optimum = (0, 0)
    sol = backtracking(variables[:], variables_range, optimum, 0)
    print('the best solution')
    print(f'{sol[0]} pants, {sol[1]} t-shirts')
    print(f'benefit {calculate_solution(sol)}')


init()

