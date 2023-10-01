import "strings"

func reverseWords(s string) string {
    res := strings.Fields(s)
    for i, word := range res {
        revWord := reverseString(word)
        res[i] = revWord
    }

    return strings.Join(res, " ")

}

func reverseString(s string) string {
    runes := []rune(s)
    l, r := 0, len(runes) - 1
    for l < r {
        runes[l], runes[r] = runes[r], runes[l]
        l++
        r--
    }

    return string(runes)
}