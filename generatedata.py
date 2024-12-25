import random

for N in range(6_000_000, 50_000_000, 100_0000):
    with open(f"data/num{N}.txt", "w") as file:
        for i in range(N):
            file.write(f"{random.randint(1, 500_000)}\t")