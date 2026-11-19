import (
    "slices"
    "fmt"
    )

func minimizeSum(nums []int) int {
    slices.Sort(nums)
    // nums[0] = nums[2]
    // nums[1] = nums[2]
    chMax := (nums[len(nums) - 1] - nums[2])
    chMin := (nums[len(nums) - 3] - nums[0])
    chfl := (nums[len(nums) - 2] - nums[1])
    return min(chMax, chMin, chfl)
}