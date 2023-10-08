def BracketCombinations(num):
  if num == 0:
    return 1
    
  dp = [0] * (num + 1)
  dp[0] = 1
    
  for i in range(1, num + 1):
    print('dp', dp)
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]
  
  return dp[num]

# keep this function call here 
print(BracketCombinations(0))
print(BracketCombinations(1))
print(BracketCombinations(2))
print(BracketCombinations(3))
print(BracketCombinations(4))
print(BracketCombinations(5))
