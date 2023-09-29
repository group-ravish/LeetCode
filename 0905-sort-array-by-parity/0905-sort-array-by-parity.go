func sortArrayByParity(nums []int) []int {
    eve := []int{}
    odd := []int{}

    for _, i := range nums {
        if i % 2 == 0 {
            eve = append(eve, i)
        } else {
            odd = append(odd, i)
        }
    }
    
    eve = append(eve, odd...)
    return eve
}