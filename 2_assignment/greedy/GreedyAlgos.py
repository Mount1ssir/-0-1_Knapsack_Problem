import time
n_20 = 20 ; W_20 = 35 ; u_20 = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6] ; w_20 = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]
n_100 = 100 ; W_100 = 1400 ; u_100 = [4, 7, 8, 2, 1, 1, 9, 5, 5, 3, 9, 9, 5, 4, 4, 9, 3, 7, 9, 7,10, 9, 1, 9, 5, 3, 2, 6, 2, 2, 3, 10, 4, 2, 4, 5, 9, 2, 5, 8,5, 2, 9, 6, 1, 8, 10, 6, 1, 8, 6, 4, 8, 8, 8, 1, 8, 9, 9, 3,5, 6, 3, 7, 6, 8, 8, 3, 4, 3, 10, 4, 6, 4, 2, 2, 6, 10, 10, 8,3, 7, 7, 10, 8, 7, 1, 1, 4, 8, 5, 6, 3, 9, 8, 7, 6, 5, 5, 1]; w_100 = [18, 16, 18, 11, 13, 17, 10, 19, 14, 17, 19, 12, 17, 10, 20, 16, 15, 16, 10, 20, 11, 20, 14, 16, 19, 13, 16, 19, 16, 12, 17, 11, 16, 17, 12, 12, 19, 13, 18, 14,14, 16, 11, 10, 10, 19, 12, 13, 20, 20, 19, 12, 12, 18, 17, 20, 15, 16, 18, 10,15, 19, 12, 16, 12, 15, 11, 12, 20, 20, 15, 18, 15, 13, 19, 15, 15, 11, 18, 11,15, 18, 10, 18, 19, 12, 16, 17, 16, 17, 12, 12, 14, 15, 15, 15, 12, 16, 16, 12] 
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

