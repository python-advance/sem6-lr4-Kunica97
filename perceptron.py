def sigmoid(x):
    import math
    return 1 / (1 + math.exp(-x))

def get_theta(operation):
    if operation == 'or':
        theta = [-10, 20, 20]

    elif operation == 'and':
        theta = [-30, 20, 20]

    elif operation == 'not':
        theta = [3, -30]
    return theta

def pc_or_and(input_X, theta, bias_X=1):
    results = []
    for i in range(len(input_X)):
        result = sigmoid(bias_X * theta[0] + input_X[i][0] * theta[1] + input_X[i][1] * theta[2])
        if (result >= 0.9):
            result = 1
        else:
            result = 0
        results.append(result)
    return results

def pc_not(input_X, theta, bias_X=1):
    results = []
    for i in range(len(input_X)):
        result = sigmoid(bias_X * theta[0] + input_X[i] * theta[1])
        if (result >= 0.5):
            result = 1
        else:
            result = 0
        results.append(result)
    return results

def pc_xor(input_X, theta_or, theta_and, theta_not):
    new_input_X = []
    a1 = pc_or_and(input_X, theta_or)
    for item in input_X:
        new_input_X.append(tuple(pc_not(list(item), theta_not)))
    a2 = pc_or_and(new_input_X, theta_or)
    a1a2 = list(zip(a1, a2))
    result = pc_or_and(a1a2, theta_and)
    return result, a1, a2

def pc_xnor(input_X, theta_or, theta_and, theta_not):
    new_input_X = []
    a1 = pc_or_and(input_X, theta_and)
    for item in input_X:
        new_input_X.append(tuple(pc_not(list(item), theta_not)))
    a2 = pc_or_and(new_input_X, theta_and)
    a1a2 = list(zip(a1, a2))
    result = pc_or_and(a1a2, theta_or)
    return result, a1, a2

X = [(0, 0), (0, 1), (1, 0), (1, 1)]
theta_or = get_theta('or')
theta_and = get_theta('and')
theta_not = get_theta('not')

print('OR:', pc_or_and(X, theta_or))
print('AND:', pc_or_and(X, theta_and))
print('XOR:', pc_xor(X, theta_or, theta_and, theta_not)[0])
print('XNOR:', pc_xnor(X, theta_or, theta_and, theta_not)[0])