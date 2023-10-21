def new_21_game(n: int, k: int, max_pts: int) -> float:
    if k == 0 or n >= k + max_pts:
        return 1.0
    
    window_sum = 1.0
    prob = 0.0

    dp = [0.0] * (n + 1)
    dp[0] = 1.0

    for i in range(1, n + 1):
        dp[i] = window_sum / max_pts
        
        if i < k:
            window_sum += dp[i]
        else:
            prob += dp[i]
        
        if i >= max_pts:
            window_sum -= dp[i - max_pts]
        
    return prob

print(new_21_game(10, 1, 10))
print(new_21_game(6, 1, 10))
print(new_21_game(21, 17, 10))
print(new_21_game(0, 0, 1))
print(new_21_game(1, 0, 1))