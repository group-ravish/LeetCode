func majorityElement(nums []int) []int {
    count := make(map[int]int)
    res := []int{}

    for i := 0; i < len(nums); i++ {
        count[nums[i]]++
    }

    for k, v := range count {
        if v > len(nums)/3 {
            res = append(res, k)
        }
    }

    return res   
}
