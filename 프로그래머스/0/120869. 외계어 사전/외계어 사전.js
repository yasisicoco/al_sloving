function solution(spell, dic) {
    const sortedSpell = spell.sort()
    let longSorted = 0
    for (let d of dic) {
        const sortedDic = [...d].sort()
        
        // 순회길이
        if (sortedSpell.length > sortedDic.length) {
            longSorted = sortedSpell.length     
        } else {
            longSorted = sortedDic.length
        }
        let flag = false
        
        for (let i = 0; i < longSorted; i++) {
            if (sortedSpell[i] !== sortedDic[i]) {
                flag = false
                break
            } else {
                flag = true
            }
        }
        
        if (flag === true) {
            return 1
        }
    }
    
    return 2
}