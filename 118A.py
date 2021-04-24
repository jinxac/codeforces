class Solution:
  def solve(self, string):
    res = []
    for element in string:
      if element.lower() in set(['a', 'e', 'i','o','u', 'y']):
        continue

      res.append('.')
      res.append(element.lower())

    return ''.join(res)




if __name__ == "__main__":
  string = input()
  s = Solution()
  print(s.solve(string))
