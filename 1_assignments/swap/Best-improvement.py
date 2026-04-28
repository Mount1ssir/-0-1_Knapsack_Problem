n = 20
W = 35
u = [4, 2, 1, 2, 10, 2, 2, 1, 3, 2, 5, 3, 2, 8, 5, 2, 6, 12, 14, 6]
w = [12, 2, 1, 1, 4, 1, 2, 1, 2, 1, 3, 2, 1, 5, 3, 2, 4, 6, 7, 3]

def get_weight(x):
    return sum(w[i]*x[i] for i in range(n))

def get_value(x):
    return sum(u[i]*x[i] for i in range(n))

def Swap_Best_Improvement():
    x = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
    iteration = 0

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
            iteration += 1
        else:
            break

    return x, iteration
x,iteration = Swap_Best_Improvement()
print (get_value(x))
print(get_weight(x))
print(iteration)