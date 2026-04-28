import random

def generate_10k_data(filename):
    n = 10000
    random.seed(42) # For reproducibility in your report
    
    # Generating utilities and weights in realistic ranges
    u = [random.randint(1, 10) for _ in range(n)]
    w = [random.randint(10, 20) for _ in range(n)]
    W = int(sum(w) * 0.4) # Capacity at 40%
    
    with open(filename, 'w') as f:
        f.write(f"n = {n};\n")
        f.write(f"W = {W};\n\n")
        
        f.write("u = [\n")
        f.write(", ".join(map(str, u)))
        f.write("\n];\n\n")
        
        f.write("w = [\n")
        f.write(", ".join(map(str, w)))
        f.write("\n];\n")

generate_10k_data("n10000.dat")
print("n10000.dat has been generated successfully.")