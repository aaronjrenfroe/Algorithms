# Returns the nth number in the fibonacci sequence
def fib_rec(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_rec(10))