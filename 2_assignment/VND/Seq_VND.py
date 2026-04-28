import time
n_20 = 20 ; W_20 = 35 ; u_20 = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6] ; w_20 = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]
n_100 = 100 ; W_100 = 1400 ; u_100 = [4, 7, 8, 2, 1, 1, 9, 5, 5, 3, 9, 9, 5, 4, 4, 9, 3, 7, 9, 7,10, 9, 1, 9, 5, 3, 2, 6, 2, 2, 3, 10, 4, 2, 4, 5, 9, 2, 5, 8,5, 2, 9, 6, 1, 8, 10, 6, 1, 8, 6, 4, 8, 8, 8, 1, 8, 9, 9, 3,5, 6, 3, 7, 6, 8, 8, 3, 4, 3, 10, 4, 6, 4, 2, 2, 6, 10, 10, 8,3, 7, 7, 10, 8, 7, 1, 1, 4, 8, 5, 6, 3, 9, 8, 7, 6, 5, 5, 1]; w_100 = [18, 16, 18, 11, 13, 17, 10, 19, 14, 17, 19, 12, 17, 10, 20, 16, 15, 16, 10, 20, 11, 20, 14, 16, 19, 13, 16, 19, 16, 12, 17, 11, 16, 17, 12, 12, 19, 13, 18, 14,14, 16, 11, 10, 10, 19, 12, 13, 20, 20, 19, 12, 12, 18, 17, 20, 15, 16, 18, 10,15, 19, 12, 16, 12, 15, 11, 12, 20, 20, 15, 18, 15, 13, 19, 15, 15, 11, 18, 11,15, 18, 10, 18, 19, 12, 16, 17, 16, 17, 12, 12, 14, 15, 15, 15, 12, 16, 16, 12] 


def get_weight(x, n, w):
    return sum(w[i]*x[i] for i in range(n))

def get_value(x, n, u):
    return sum(u[i]*x[i] for i in range(n))

# 1-Flip
def local_search_1flip(x, n, W, u, w):
    while True:
        best_flip = -1
        max_gain = 0
        for i in range(n):
            y = list(x)
            y[i] = 1 - x[i]
            if get_weight(y, n, w) <= W:
                gain = get_value(y, n, u) - get_value(x, n, u)
                if gain > max_gain:
                    max_gain = gain
                    best_flip = i
        if best_flip != -1:
            x[best_flip] = 1 - x[best_flip]
        else:
            break
    return x

# 2-Flip
def local_search_2flip(x, n, W, u, w):
    while True:
        best_pair = (-1, -1)
        max_gain = 0
        for i in range(n):
            for j in range(i+1, n):
                y = list(x)
                y[i] = 1 - x[i]
                y[j] = 1 - x[j]
                if get_weight(y, n, w) <= W:
                    gain = get_value(y, n, u) - get_value(x, n, u)
                    if gain > max_gain:
                        max_gain = gain
                        best_pair = (i, j)
        if best_pair != (-1, -1):
            i, j = best_pair
            x[i] = 1 - x[i]
            x[j] = 1 - x[j]
        else:
            break
    return x

# Neighborhood 3 : Swap
def local_search_swap(x, n, W, u, w):
    x = list(x)
    while True:
        improvement = False
        x_best = list(x)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if x[i] != x[j]:
                    y = list(x)
                    y[i], y[j] = y[j], y[i]
                    if get_weight(y, n, w) <= W and get_value(y, n, u) > get_value(x_best, n, u):
                        x_best = y
                        improvement = True
        if improvement:
            x = x_best
        else:
            break
    return x

# VND : Algorithm 9
def VND(n, W, u, w):
    x = [0]*n
    neighborhoods = [local_search_1flip, local_search_2flip, local_search_swap]
    k_max = len(neighborhoods)
    k = 0
    while k < k_max:
        y = neighborhoods[k](list(x), n, W, u, w)
        if get_value(y, n, u) > get_value(x, n, u):
            x = y
            k = 0
        else:
            k += 1
    return x

# exe for n=20
start = time.perf_counter()
result1 = VND(n_20, W_20, u_20, w_20)
end = time.perf_counter()

print("================")
print(f"Value:             {get_value(result1, n_20, u_20)}")
print(f"Weight:            {get_weight(result1, n_20, w_20)}")
print(f"Execution Time:    {(end - start)*1000:.4f} ms")

# exe for n=100
start = time.perf_counter()
result2 = VND(n_100, W_100, u_100, w_100)
end = time.perf_counter()

print("================")
print(f"Value:             {get_value(result2, n_100, u_100)}")
print(f"Weight:            {get_weight(result2, n_100, w_100)}")
print(f"Execution Time:    {(end - start)*1000:.4f} ms")