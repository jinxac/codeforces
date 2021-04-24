class Solution:
  def solve(self, word):
    word = list(word)
    word[0] = word[0].upper()
    return ''.join(word)

if __name__ == "__main__":
  word = input()
  s = Solution()
  print(s.solve(word))
  
