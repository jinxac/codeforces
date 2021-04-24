class Solution:
  def solve(self, string):
    '''
    00100110111111101
    '''
    start = 0
    end = 1
    res = 0
    
    while end < len(string):
      while end < len(string) and string[end] == string[start]:
        end += 1
      res = max(res, end - start)
      if res >= 7:
        return "YES"
      start = end
      end += 1
    
    return "NO"
    



if __name__ == "__main__":
  string = input()
  s = Solution()
  print(s.solve(string))
