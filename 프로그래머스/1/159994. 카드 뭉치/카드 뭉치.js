function solution(cards1, cards2, goal) {
    let index1 = 0, index2 = 0;
    
    for (word of goal) {
        if (cards1[index1] === word) {
            index1++
        } else if (cards2[index2] === word) {
            index2++
        } else {
            return "No"
        }
    }
    return "Yes"
}