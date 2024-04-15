class Solution(object):
  def __init__(self):
    self.memo = [0, 1]
    self.counter = 1
    
  def reset_counter(self):
    self.counter = 1

  def fib(self, n: int):
    print(f"tick: {self.counter}")
    self.counter += 1
    
    #Base Case
    if (len(self.memo) - 1 >= n):
      return self.memo[-(n + 1):]
      
    #Recursive Case
    else:
      self.memo.append(self.memo[len(self.memo) - 1] + self.memo[len(self.memo) - 2])
      return self.fib(n)


solve = Solution()
print(f"{solve.fib(5)}")
solve.reset_counter()

print(f"{solve.fib(5)}")
