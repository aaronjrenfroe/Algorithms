# Given list of sorted integers
# Returns number/count of subsets with length 3 [i, j, k]
# where j % i == 0 and k % j == 0
def count_tripples(my_set):
  if(len(my_set) < 3):
    return 0

  pair_count = [0]*len(my_set)

  for i in range(1,len(my_set) - 1):
    for j in range(0,i):
      if my_set[i] % my_set[j] == 0:
        pair_count[i] += 1

  tripple_count = 0

  for i in range(2,len(my_set)):
    for j in range(1,i):
      if my_set[i] % my_set[j] == 0:
        tripple_count += pair_count[j]

  return tripple_count

numbers = [1,1,1]
print(count_tripples([1,1,1])) # 1
print(count_tripples([1, 2, 3, 4, 5, 6])) # 3