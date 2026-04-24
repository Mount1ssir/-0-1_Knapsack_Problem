n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]

def get_weight(x):
  return sum(w[i]*x[i] for i in range(n))

def get_value(x):
  return sum(u[i]*x[i] for i in range(n))

def Flip_local_search():
  x = [0]*n
  iteration = 0
  improvement = False
  while not improvement:
    
    for i in range(n):
      x_prime = list(x)
      x_prime[i] = 1- x[i]
      if get_weight(x_prime) <= W and get_value(x_prime) > get_value(x):
        x = x_prime
        improvement= True
        iteration += 1
        
  return x
results = Flip_local_search()
print(f"Solution Vector x: {results}")
print(f"solution :     {get_value(results)}")
print(f"the Weight:      {get_weight(results)}")