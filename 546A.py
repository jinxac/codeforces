class Solution:
  def solve(self, banana_cost, available_amount, count):
    total_amount = 0 
    for i in range(1, count+1):
      total_amount += banana_cost*i
    
    return total_amount - available_amount


if __name__ == "__main__":
  trimmed_input = input().split()
  x, y, z =[int(x) for x in trimmed_input]
  s = Solution()
  print(s.solve(x,y,z))
