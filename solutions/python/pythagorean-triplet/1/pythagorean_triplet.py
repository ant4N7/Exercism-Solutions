from math import sqrt

def triplets_with_sum(n):
    N = float(n)
    triplets = []
    for c in range(int(N / 2) - 1, int((sqrt(2) - 1) * N), -1):
        D = sqrt(c ** 2 - N ** 2 + 2 * N * c)
        if D == int(D):
            triplets.append([int((N - c - D) / 2), int((N - c + D) / 2), c])
    return triplets
