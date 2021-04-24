class Solution:
  def solve(self, str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    p1 = 0
    p2 = 0
    
    while p1 < len(str1) and p2 < len(str2):
      if str1[p1] < str2[p2]:
        return - 1
      
      if str1[p1] > str2[p2]:
        return 1
      
      p1 += 1
      p2 += 1
    
    return 0


if __name__ == "__main__":
  str1 = input()
  str2 = input()
  s = Solution()
  print(s.solve(str1, str2))
