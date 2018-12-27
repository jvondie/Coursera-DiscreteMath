def lcm(a, b):
  assert a > 0 and b > 0
  p = a*b

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a

  gcd = max(a,b)


  return p/gcd
