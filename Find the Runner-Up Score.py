if __name__ == '__main__': n = int(input()) arr = list(map(int, input().split())) nums= list(set(arr)) nums.sort(reverse=True) print(nums[1])
