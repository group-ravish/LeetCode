func numIdenticalPairs(nums []int) int {
    count := make(map[int]int)
    var res int

    for _, num := range nums {
        res += count[num]
        count[num]++
    }

    return res
}