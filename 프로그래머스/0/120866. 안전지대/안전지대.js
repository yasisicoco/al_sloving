function solution(board) {
    const col = board.length
    const row = board[0].length
    
    function danger(arr, i, j) {
        const a = [0, 1, 0, -1, -1, -1, 1, 1];
        const b = [1, 0, -1, 0, -1, 1, -1, 1];

        for (let k = 0; k < 8; k++) {
            const ni = i + a[k];
            const nj = j + b[k];
            if (ni >= 0 && ni < col && nj >= 0 && nj < row && arr[ni][nj] === 0) {
                arr[ni][nj] = 2;
            }
        }
    }
    
    
    for (let i = 0; i < col; i++) {
        for (let j = 0; j < row; j++) {
            if (board[i][j] === 1) {
                danger(board, i, j)
            }
        }
    }
    
    let cnt = 0
    board.forEach(item => item.forEach(index => index === 0 ? cnt++ : cnt))
    return cnt
}