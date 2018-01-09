def explosive_baby(M, F): # ;)
  steps = 0

  m = int(M)
  f = int(F)
  
  while m != 1 or f != 1:
    if m == 1:
      steps += f - 1
      break
    if f == 1:
      steps += m - 1
      break

    if m < f:
      if m == 0:
        return 'impossible'
      steps += int(f / m)
      f %= m
    else:
      if f == 0:
        return 'impossible'
      steps += int(m / f)
      m %= f

  return str(steps)




print(explosive_baby('4', '7'))