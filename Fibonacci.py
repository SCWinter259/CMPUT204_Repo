# Dynamic Programming Fibonacci
def DynFib(n):
    results = []
    results.append(0)
    results.append(1)
    for i in range(2, n):
        results.append(results[i - 1] + results[i - 2])

    return results[len(results) - 1]