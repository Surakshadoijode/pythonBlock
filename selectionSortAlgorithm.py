n=int(input())
nums=list(map(int,input().split()))

def performSelectionSort(nums):
    n = len(nums)
    for fixThisIndex in range(n - 1, 0, -1):
        maxEle = nums[fixThisIndex]
        maxEleIndex = fixThisIndex 
 
        for index in range(fixThisIndex):
            if nums[index] > maxEle:
                maxEleIndex = index 
                maxEle = nums[index]

        if fixThisIndex != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp
performSelectionSort(nums)
print(*nums)
