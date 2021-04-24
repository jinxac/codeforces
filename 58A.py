class Solution:
  def solve(self, string):
    search_string = "hello"
    pos = 0
    
    if len(string) < len(search_string):
      return "NO"
    
    for element in string:
      if pos < len(search_string) and element == search_string[pos]:
        pos += 1
      
      if pos == len(search_string):
        return "YES"
    
    return "NO"
      
      
if __name__ == "__main__":
  string = input()
  s = Solution()
  print(s.solve(string))
