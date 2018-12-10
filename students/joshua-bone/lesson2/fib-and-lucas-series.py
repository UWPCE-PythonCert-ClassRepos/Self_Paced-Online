#Joshua Bone - UW Python 210 - Lesson 2
#Fibonacci and Lucas Series Exercise

FIB_TEST = [0, 1, 1, 2, 3, 5, 8, 13]
LUC_TEST = [2, 1, 3, 4, 7, 11, 18, 29]

def sumSeries(n, a=0, b=1):
  if n<=0: raise ValueError("Series index must be >= 1, got %d." % (n))
  if n<=2: return [a, b][n - 1]
  for i in range(3, n + 1): a, b = b, a + b
  return b

if __name__ == "__main__":
  fib_out = [sumSeries(i+1) for i in range(8)]
  assert fib_out == FIB_TEST
  print("Passed the Fibonacci Series test: ", fib_out)
  luc_out = [sumSeries(i+1, 2, 1) for i in range(8)]
  assert luc_out == LUC_TEST
  print("Passed the Lucas Series test: ", luc_out)
