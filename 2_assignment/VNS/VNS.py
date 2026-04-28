import random
import time

n_20 = 20 ; W_20 = 35 
u_20 = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6] 
w_20 = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]


n_100 = 100 ; W_100 = 1400 
u_100 = [4, 7, 8, 2, 1, 1, 9, 5, 5, 3, 9, 9, 5, 4, 4, 9, 3, 7, 9, 7, 10, 9, 1, 9, 5, 3, 2, 6, 2, 2, 3, 10, 4, 2, 4, 5, 9, 2, 5, 8, 5, 2, 9, 6, 1, 8, 10, 6, 1, 8, 6, 4, 8, 8, 8, 1, 8, 9, 9, 3, 5, 6, 3, 7, 6, 8, 8, 3, 4, 3, 10, 4, 6, 4, 2, 2, 6, 10, 10, 8, 3, 7, 7, 10, 8, 7, 1, 1, 4, 8, 5, 6, 3, 9, 8, 7, 6, 5, 5, 1]
w_100 = [18, 16, 18, 11, 13, 17, 10, 19, 14, 17, 19, 12, 17, 10, 20, 16, 15, 16, 10, 20, 11, 20, 14, 16, 19, 13, 16, 19, 16, 12, 17, 11, 16, 17, 12, 12, 19, 13, 18, 14, 14, 16, 11, 10, 10, 19, 12, 13, 20, 20, 19, 12, 12, 18, 17, 20, 15, 16, 18, 10, 15, 19, 12, 16, 12, 15, 11, 12, 20, 20, 15, 18, 15, 13, 19, 15, 15, 11, 18, 11, 15, 18, 10, 18, 19, 12, 16, 17, 16, 17, 12, 12, 14, 15, 15, 15, 12, 16, 16, 12]
 
def get_weight(x, w):
    return sum(w[i] * x[i] for i in range(len(x)))

def get_value(x, u):
    return sum(u[i] * x[i] for i in range(len(x)))

def shaking(x, k, n, W, w):
    y = list(x)
    for _ in range(k):
        i = random.randint(0, n - 1)
        y[i] = 1 - y[i]
        if get_weight(y, w) > W:
            y[i] = 1 - y[i] 
    return y

# --- Local Search Neighborhoods ---
def local_search_1flip(x, n, W, u, w):
    x = list(x)
    while True:
        improvement = False
        for i in range(n):
            y = list(x)
            y[i] = 1 - y[i]
            if get_weight(y, w) <= W and get_value(y, u) > get_value(x, u):
                x = y
                improvement = True
                break
        if not improvement: break
    return x

def local_search_2flip(x, n, W, u, w):
    x = list(x)
    while True:
        improvement = False
        for i in range(n):
            for j in range(i+1, n):
                y = list(x)
                y[i] = 1 - y[i]
                y[j] = 1 - y[j]
                if get_weight(y, w) <= W and get_value(y, u) > get_value(x, u):
                    x = y
                    improvement = True
                    break
            if improvement: break
        if not improvement: break
    return x

def local_search_swap(x, n, W, u, w):
    x = list(x)
    while True:
        improvement = False
        for i in range(n - 1):
            for j in range(i+1, n):
                if x[i] != x[j]:
                    y = list(x)
                    y[i], y[j] = y[j], y[i]
                    if get_weight(y, w) <= W and get_value(y, u) > get_value(x, u):
                        x = y
                        improvement = True
                        break
            if improvement: break
        if not improvement: break
    return x

# 3. VNS EXECUTION WRAPPER


def VNS(n, W, u, w, time_limit=5):
    neighborhoods = [local_search_1flip, local_search_2flip, local_search_swap]
    k_max = len(neighborhoods)
    
    best = [0] * n 
    start = time.perf_counter()

    while (time.perf_counter() - start) < time_limit:
        k = 0
        while k < k_max:
            x_prime = shaking(best, k+1, n, W, w)
            x_second = neighborhoods[k](x_prime, n, W, u, w)
            
            if get_weight(x_second, w) <= W and get_value(x_second, u) > get_value(best, u):
                best = x_second
                k = 0 
            else:
                k += 1 
    
    return best, time.perf_counter() - start



# run
final_sol, exec_time = VNS(n_100, W_100, u_100, w_100, time_limit=100)

print("=== FINAL VNS RESULTS FOR n=100 ===")
print(f"Value:          {get_value(final_sol, u_100)}") 
print(f"Weight:         {get_weight(final_sol, w_100)}") 
print(f"Execution Time: {exec_time:.4f} s")