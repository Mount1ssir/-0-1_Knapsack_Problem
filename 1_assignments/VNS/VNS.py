import time
import random

n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]

def get_weight(x):
    return sum(w[i]*x[i] for i in range(n))

def get_value(x):
    return sum(u[i]*x[i] for i in range(n))

# ── Shaking
def shaking(x, k):
    y = list(x)
    flips = random.sample(range(n), k)   
    for i in flips:
        y[i] = 1 - y[i]
    while get_weight(y) > W:
        ratio = [(u[i]/w[i] if y[i] == 1 else float('inf')) for i in range(n)]
        drop = ratio.index(min(ratio))
        y[drop] = 0
    return y

# ── Local Search neighborhoods
def local_search_1flip(x):
    x = list(x)
    while True:
        improvement = False
        for i in range(n):
            y = list(x)
            y[i] = 1 - y[i]
            if get_weight(y) <= W and get_value(y) > get_value(x):
                x = y
                improvement = True
                break
        if not improvement:
            break
    return x

def local_search_2flip(x):
    x = list(x)
    while True:
        improvement = False
        for i in range(n):
            for j in range(i+1, n):
                y = list(x)
                y[i] = 1 - y[i]
                y[j] = 1 - y[j]
                if get_weight(y) <= W and get_value(y) > get_value(x):
                    x = y
                    improvement = True
                    break
            if improvement:
                break
        if not improvement:
            break
    return x

def local_search_swap(x):
    x = list(x)
    while True:
        improvement = False
        for i in range(n - 1):
            for j in range(i+1, n):
                if x[i] != x[j]:
                    y = list(x)
                    y[i], y[j] = y[j], y[i]
                    if get_weight(y) <= W and get_value(y) > get_value(x):
                        x = y
                        improvement = True
                        break
            if improvement:
                break
        if not improvement:
            break
    return x

neighborhoods     = [local_search_1flip, local_search_2flip, local_search_swap]
k_max             = len(neighborhoods)

# ── VNS
def VNS(x, time_limit=20):
    best   = list(x)
    start  = time.perf_counter()

    while (time.perf_counter() - start) < time_limit:  
        k = 0                                            
        while k < k_max:
            x_prime  = shaking(best, k+1)              
            x_second = neighborhoods[k](x_prime)        
            if get_weight(x_second) <= W and get_value(x_second) > get_value(best):
                best = x_second                         
                k    = 0                                
            else:
                k += 1                                 

    return best

# ── Run ───────────────────────────────────────────────────────────────────
x0     = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

start  = time.perf_counter()
result = VNS(x0, time_limit=100)
end    = time.perf_counter()

print(f"Solution Vector x: {result}")
print(f"Value:             {get_value(result)}")
print(f"Weight:            {get_weight(result)}")
print(f"Execution Time:    {(end - start):.4f} s")