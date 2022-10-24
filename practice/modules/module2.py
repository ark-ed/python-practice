def findmax(list):
  i = list[0]
  for x in list:
    if i < x:
      i = x
  return i