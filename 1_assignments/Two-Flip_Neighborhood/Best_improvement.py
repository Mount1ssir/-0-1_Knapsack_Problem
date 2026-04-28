n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]

def get_weight(x):
    return sum(w[i]*x[i] for i in range(n))

def get_value(x):
    return sum(u[i]*x[i] for i in range(n))

def Best_Improvement_Search_2():
    x = [0] * n
    iteration = 0

    while True:
        best_pair = (-1, -1)
        max_gain = 0

        for i in range(n):
            for j in range(i+1, n):             # all unique pairs
                x_prime = list(x)
                x_prime[i] = 1 - x[i]          # flip bit i
                x_prime[j] = 1 - x[j]          # flip bit j

                if get_weight(x_prime) <= W:
                    gain = get_value(x_prime) - get_value(x)
                    if gain > max_gain:          # track the BEST gain across all pairs
                        max_gain = gain
                        best_pair = (i, j)

        if best_pair != (-1, -1):               # apply only the single best pair found
            i, j = best_pair
            x[i] = 1 - x[i]
            x[j] = 1 - x[j]
            iteration += 1
        else:
            break

    return x, iteration

results, iters = Best_Improvement_Search_2()
print(f"Solution Vector x: {results}")
print(f"Value:             {get_value(results)}")
print(f"Weight:            {get_weight(results)}")
print(f"Iterations:        {iters}")