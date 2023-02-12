def even_odd(arglist) -> float:
  if sum(arglist[1::2]) != 0:
    return sum(arglist[1::2])/sum(arglist[0::2])
  else:
    return 0

