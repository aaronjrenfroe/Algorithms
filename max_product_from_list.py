# Given a list of integers
# Return the maximim product of a subset of the list

def max_product(int_list):
  if len(int_list) == 0:
    return 0
  elif len(int_list) == 1:
    return int_list[0]

  product = 1
  for val in [val for val in int_list if val > 0]:
    product *= val

  neg_list = [val for val in int_list if val < 0]

  if len(neg_list) % 2 == 1:
    neg_list.sort()
    neg_list = neg_list[:-1]

  for val in neg_list:
    product *= val

  return product

print(max_product([2, -3, 1, 0, -6])) # 36
print(max_product([2, 0, 2, 2, 1])) # 8
print(max_product([-2, -3, 4, -6])) # 72
