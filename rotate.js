var rotate = function(matrix) {
    matrix.reverse()
    for (let i = 0; i < matrix.length; i++) {
        for (let j = i+1; j < matrix[i].length; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        }
    }
    return matrix
};