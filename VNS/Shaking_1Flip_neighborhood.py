import random

n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]
x = [0] * n

def is_feasible(sol):
    return sum(w[i] * sol[i] for i in range(n)) <= W

def objective(sol):
    return sum(u[i] * sol[i] for i in range(n))

def shaking_1flip(x, r):
    x_prime = x.copy()

    for t in range(1, r + 1):
        i = random.randint(0, n - 1)
        x_double_prime = x_prime.copy()
        x_double_prime[i] = 1 - x_double_prime[i]

        if is_feasible(x_double_prime):
            x_prime = x_double_prime

    return x_prime

random.seed(42)
r = 10

print("Initial solution :", x)
print("Initial weight   :", sum(w[i] * x[i] for i in range(n)))
print("Initial utility  :", objective(x))
print()

x_shaken = shaking_1flip(x, r)

print("Shaken solution  :", x_shaken)
print("Shaken weight    :", sum(w[i] * x_shaken[i] for i in range(n)),f"(capacity W={W})")
print("Shaken utility   :", objective(x_shaken))
print("Feasible?        :", is_feasible(x_shaken))