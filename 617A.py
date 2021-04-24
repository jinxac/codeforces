class Solution:
  def solve(self, position):
    res = 0
    start = 5
    
    while position > 0:
      if position < start:
        start -= 1
      
      res += 1
      position -= start
    
    return res
      

if __name__ == "__main__":
  position = int(input())
  s = Solution()
  print(s.solve(position))

