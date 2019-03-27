import math
if __name__ == '__main__':
  instr = raw_input()
  n, m, a = list(map(int, instr.strip().split(" ")))
  r = n/a
  if n%a !=0:
    r += 1
  c = m/a
  if m%a !=0:
    c += 1
  r = 1 if r<=0 else r
  c = 1 if c<=0 else c
  print(r*c)
