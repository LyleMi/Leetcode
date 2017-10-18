/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var used = new Array(3);
    for (let i = 0; i < 3; i++) {
        used[i] = new Array(9);
        for (let j = 0; j < 9; j++) {
            used[i][j] = new Array(9);
            for (let k = 0; k < 9; k++) {
                used[i][j][k] = false;
            }
        }
    }
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            if (board[i][j] != '.') {
                let num = parseInt(board[i][j]) - 1;
                let k = parseInt(i / 3) * 3 + parseInt(j / 3);
                if (used[0][i][num] || used[1][j][num] || used[2][k][num])
                    return false;
                used[0][i][num] = used[1][j][num] = used[2][k][num] = true;
            }
        }
    }
    return true;
};