n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]

def get_weight(x):
  return sum(w[i]*x[i] for i in range(n))

def get_value(x):
  return sum(u[i]*x[i] for i in range(n))

def Best_Improvement_Search():
    x = [0] * n 
    while True:
        best_flip = -1
        max_gain = 0
        
        for i in range(n):
            x_prime = list(x)
            x_prime[i] = 1 - x[i]  

            if get_weight(x_prime) <= W:
                gain = get_value(x_prime) - get_value(x)
                if gain > max_gain:
                    max_gain = gain
                    best_flip = i
    
        if best_flip != -1:
            x[best_flip] = 1 - x[best_flip]
        else:
            break
            
    return x

results_best = Best_Improvement_Search()
print(f"Solution Vector x: {results_best}")
print(f"solution :      {get_value(results_best)}")
print(f"the Weight:      {get_weight(results_best)}")