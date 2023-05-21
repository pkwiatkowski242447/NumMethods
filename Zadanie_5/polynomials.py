def evaluate_polynomial(coefficients, x):
    n = len(coefficients)
    result = coefficients[n-1]
    for i in range(n-2, -1, -1):
        result = result*x + coefficients[i]
    return result
