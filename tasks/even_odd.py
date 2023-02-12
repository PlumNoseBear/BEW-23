def even_odd(arglist) -> float:
  odds = 0
  nodds=0
  for i in arglist:
    if i%2==0:
      odds=odds+i
    else:
      nodds=nodds+i
    
  return odds/nodds if nodds !=0 else 0
