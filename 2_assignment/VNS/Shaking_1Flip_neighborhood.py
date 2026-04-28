import random
import time
n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]
x = [0] * n

def objective(sol):
    return sum(u[i] * sol[i] for i in range(len(sol)))

def is_feasible(sol):
    total_weight = sum(w[i] * sol[i] for i in range(len(sol)))
    return total_weight <= W

def shaking_1flip_neighborhood(x, r):
    
    x_prime = list(x) 
    n = len(x_prime)
    
    for t in range(1, r + 1):
        i = random.randint(0, n - 1)
        
        x_double_prime = list(x_prime)
        
        x_double_prime[i] = 1 - x_double_prime[i]
        
        if is_feasible(x_double_prime):
            x_prime = list(x_double_prime)
            
    return x_prime

x_initial = [0] * n
r_intensity = 10 
print("--- BEFORE SHAKING ---")
print(f"Solution x: {x_initial}")
print(f"Utility:    {objective(x_initial)}")
print(f"Weight:     {sum(w[i] * x_initial[i] for i in range(n))}")
print("-" * 40)

start_time = time.perf_counter()
x_shaken = shaking_1flip_neighborhood(x_initial, r_intensity)
end_time = time.perf_counter()

print("--- AFTER SHAKING ---")
print(f"Solution x': {x_shaken}")
print(f"Utility:     {objective(x_shaken)}")
print(f"Weight:      {sum(w[i] * x_shaken[i] for i in range(n))} (Max W={W})")
print(f"Time Taken:  {(end_time - start_time)*1000:.4f} ms")