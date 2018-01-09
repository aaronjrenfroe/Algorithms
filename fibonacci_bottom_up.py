# Returns the nth number in the fibonacci sequence
def fib_buttom_up(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  fib_list = n*[None]
  fib_list[0] = 1
  fib_list[1] = 1

  for i in range(2, n):
    fib_list[i] = fib_list[i-1]+ fib_list[i - 2]
  
  return fib_list[-1]

print(fib_buttom_up(1))