def triplets_with_sum(target_sum):
    return [[a, b, target_sum - a - b] 
            for a in range(1, target_sum // 3 + 1) 
            for b in range(a, (target_sum - a) // 2 + 1) 
            if a * a + b * b == (target_sum - a - b) * (target_sum - a - b)]
