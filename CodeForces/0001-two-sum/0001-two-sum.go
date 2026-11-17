import "fmt"

func twoSum(nums []int, target int) []int {
    var hash = map[int]int{}
    for i, num := range nums {
        hash[num] = i
    }
    var result []int
    for i, num := range nums {
        if targetIndex, ex := hash[target - num]; ex {
            if targetIndex != i {
                result = append(result, i)
                result = append(result, targetIndex)
                return result
            }
            // fmt.Println(i, num, targetIndex)
            // result = append(value)
        }
    }

    return []int{1, 2};
}