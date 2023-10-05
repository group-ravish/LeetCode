import "fmt"
func majorityElement(nums []int) []int {
    count := make(map[int]int)
    res := []int{}

    for n := 0; n < len(nums); n++ {
        count[nums[n]]++
    }

    for k, v := range count {
        if v > len(nums)/3 {
            res = append(res, k)
        }
    }

    return res   
}