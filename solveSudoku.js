/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {

    let solve = function(board) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (let k = 1; k <= 9; k++) {
                        if (isValid(board, i, j, k)) {
                            board[i][j] = '' + k
                            if (solve(board)) {
                                return true
                            } else {
                                board[i][j] = '.'
                            }
                        }
                    }
                    return false
                }
            }
        }
        return true
    }

    let isValid = function(board, row, col, c) {
        for (let i = 0; i < 9; i++) {
            if (board[i][col] != '.' && board[i][col] == c) return false
            if (board[row][i] != '.' && board[row][i] == c) return false
            let t = board[3 * Math.floor(row / 3) + Math.floor(i / 3)][3 * Math.floor(col / 3) + i % 3]
            if (t != '.' && t == c) return false
        }
        return true
    }

    if (!board.length) return
    solve(board)
};