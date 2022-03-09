
def par_bueno(nums):
  cont = 0
  for i in range(len(nums)):
    for j in range(len(nums)):
      if (nums[i] == nums[j]) and (i < j):
        cont += 1
  return cont


def main():
  nums = [1,2,3,1,1,3]
  print(par_bueno(nums))

main()
