function solution(babbling) {
    const arr = ['aya', 'ye', 'woo', 'ma']
    let cnt = 0
    
    for (let bab of babbling) {
        let temp = bab
        for (let word of arr) {
            // 'wyeoo' 의 경우 'ye'가 사라졌을때 'woo'가 되지않게하기위해 ' '공백 추가
            temp = temp.replace(word, ' ')
        }
        if (temp.trim() === '') {
            cnt++
        }
    }
    
    return cnt
}