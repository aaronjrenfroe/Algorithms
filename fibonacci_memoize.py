# Returns the nth number in the fibonacci sequence
def fib_memo(n, memo):
  if n == 0:
    return 0
  elif memo[n] != None: 
    return memo[n]
  elif n == 1 or n == 2:
    memo[n] = 1
  else:
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
  return memo[n]

# memo initialiseation cen be done differntly 
# but this is the simplest method that keeps fib_memo clean
# inorder to understand what's going on.
n = 0
memo = (n+1)*[None]
print(fib_memo(n, memo))