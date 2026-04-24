import time

n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]

def get_weight(x):
    return sum(w[i]*x[i] for i in range(n))

def get_value(x):
    return sum(u[i]*x[i] for i in range(n))

# 1-Flip
def local_search_1flip(x):
    while True:
        best_flip = -1
        max_gain = 0
        
        for i in range(n):
            y = list(x)
            y[i] = 1 - x[i]  

            if get_weight(y) <= W:
                gain = get_value(y) - get_value(x)
                if gain > max_gain:
                    max_gain = gain
                    best_flip = i
    
        if best_flip != -1:
            x[best_flip] = 1 - x[best_flip]
        else:
            break
            
    return x

# 2-Flip
def local_search_2flip(x):
    while True:
        best_pair = (-1, -1)
        max_gain = 0

        for i in range(n):
            for j in range(i+1, n):             
                y = list(x)
                y[i] = 1 - x[i]          
                y[j] = 1 - x[j]         

                if get_weight(y) <= W:
                    gain = get_value(y) - get_value(x)
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

# ── Neighborhood 3 : Swap
def local_search_swap(x):
    x = list(x)
    while True:
        improvement = False
        x_best = list(x)               

        for i in range(n - 1):
            for j in range(i + 1, n):
                if x[i] != x[j]:
                    y = list(x)
                    y[i], y[j] = y[j], y[i]

                    if get_weight(y) <= W and get_value(y) > get_value(x_best):  
                        x_best = y                  
                        improvement = True

        if improvement:
            x = x_best   
        else:
            break

    return x

# ── VND : Algorithm 9 
def VND():
    x = [0]*n

    neighborhoods = [local_search_1flip,local_search_2flip,local_search_swap]
    k_max = len(neighborhoods)

    k = 0                                       
    while k < k_max:
        y = neighborhoods[k](x)           
        if get_value(y) > get_value(x):   
            x = y
            k = 0                               
        else:
            k += 1                              

    return x


start = time.perf_counter()
result = VND()
end   = time.perf_counter()
print("================")
print(f"Solution Vector x: {result}")
print(f"Value:             {get_value(result)}")
print(f"Weight:            {get_weight(result)}")
print(f"Execution Time:    {(end - start)*1000:.4f} ms")