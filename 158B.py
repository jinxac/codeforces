class Solution:
  def solve(self, arr, n):
    arr.sort()
    res = 0
    start = 0
    end = len(arr) - 1
    carry = 0
    
    print(arr)

    while start < end:
      if arr[start] + arr[end] + carry > 4:
        res += 1
        end -= 1

      elif arr[start] + arr[end] + carry == 4:
        res += 1
        end -= 1
        start += 1
        carry = 0

      else:
        carry += arr[start]
        start += 1


    if start == end:
      res += 1

    return res


if __name__ == "__main__":
  n = int(input())
  arr = [int(x) for x in list(input().split())]
  s = Solution()
  print(s.solve(arr, n))
