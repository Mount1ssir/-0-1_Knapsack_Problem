import time
n_20 = 20 ; W_20 = 35 ; u_20 = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6] ; w_20 = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]
# first algo 
def max_Value_First(W, w, u):
    items = sorted(zip(u, w), key=lambda x: x[0], reverse=True)
    s_u, s_w = zip(*items)
    c = 0
    p = 0
    l=[]
    for i in range(len(s_u)):
        if c + s_w[i] <= W:
            c += s_w[i]  
            p += s_u[i]
            l=l+[s_u[i]]
    return f"solution : {p}\nchosen items : {l}\nthe weight : {c}"
# second algo
def min_Value_First(W, w, u):
    items = sorted(zip(u, w), key=lambda x: x[1])
    s_u, s_w = zip(*items)
    c = 0
    p = 0
    l=[]
    for i in range(len(s_u)):
        if c + s_w[i] <= W:
            c += s_w[i]  
            p += s_u[i]
            l=l+[s_u[i]]
    return f"solution : {p}\nchosen items : {l}\nthe weight : {c}"
    
# third algo
def max_Density(W, w, u):
    r = []
    for i in range(len(w)):
        r = r + [u[i]/w[i]]
        
    items = sorted(zip(r, u, w), key=lambda x: x[0], reverse=True)
    R, s_u, s_w = zip(*items)
    
    c = 0 # Current Weight
    p = 0 # Total Profit
    l = [] # List of chosen utilities
    
    for i in range(len(R)):
        if c + s_w[i] <= W:
            c += s_w[i]
            p += s_u[i]
            l = l + [s_u[i]]
            
    return f"solution : {p}\nchosen items : {l}\nthe weight : {c}"
# fourth algo
def H_Density(W, w, u):
    r = []
    for i in range(len(w)):
        r = r + [(u[i]**2)/w[i]]
        
    items = sorted(zip(r, u, w), key=lambda x: x[0], reverse=True)
    R, s_u, s_w = zip(*items)
    
    c = 0 # Current Weight
    p = 0 # Total Profit
    l = [] # List of chosen utilities
    
    for i in range(len(R)):
        if c + s_w[i] <= W:
            c += s_w[i]
            p += s_u[i]
            l = l + [s_u[i]]
            
    return f"solution : {p}\nchosen items : {l}\nthe weight : {c}"

# fifth algo
def reverse_Density_First(W, w, u):
    r = []
    for i in range(len(w)):
        r = r + [u[i]/w[i]]
    
    items = sorted(zip(r, u, w), key=lambda x: x[0])
    R, s_u, s_w = zip(*items)
    
    current_weight = sum(w)
    total_profit = sum(u)
    in_knapsack = [True] * len(s_u)
    i = 0
    while current_weight > W and i < len(s_w):
        current_weight -= s_w[i]
        total_profit -= s_u[i]
        in_knapsack[i] = False
        i += 1

    s=[]
    for i in range (len(s_u)) : 
        if in_knapsack[i] : 
            s=s+[s_u[i]]
            
    return f"solution : {total_profit}\nchosen items : {s}\nthe weight : {current_weight}"

start_time = time.perf_counter()
result = max_Value_First(W_20, w_20, u_20)
end_time = time.perf_counter()
print(result)
print(f"Execution Time: {end_time - start_time:.6f} seconds")
