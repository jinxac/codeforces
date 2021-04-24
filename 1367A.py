class Solution:
  def solve(self, string):
    string = list(string)
    for i in range(2, len(string), 2):
      string[i] = "/"
    
    print(string)
    return ''.join([element for element in string if element != "/"])
      


if __name__ == "__main__":
  t = int(input())
  s = Solution()
  while t:
    string = input()
    print(s.solve(string))
    t -= 1
  
