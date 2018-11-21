def swaps(a, b):
  newa = b[:2] + a[2:]
  newb = a[:2] + b[2:]

  return newa + ' ' + newb
print(swaps('abc', 'xyz'))
