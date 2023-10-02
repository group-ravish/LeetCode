func winnerOfGame(colors string) bool {
    alice := 0
    bob := 0
    for i := 1; i < len(colors) - 1; i++ {        
        if colors[i] == 'A' && colors[i-1] == 'A' && colors[i+1] == 'A' {
            alice++
        } else if colors[i] == 'B' && colors[i-1] == 'B' && colors[i+1] == 'B' {
            bob++
        }
    }
    return alice > bob
}