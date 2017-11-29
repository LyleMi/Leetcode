def exist(board, word)
    for x in 0..board.length - 1 do
        for y in 0..board[x].length - 1 do
            if existRec(board, x, y, word, 0)
                return true
            end
        end
    end
    return false
end

def existRec(board, x, y, word, i)
    if i == word.length
        return true
    end
    if x < 0 or y < 0 or x == board.length or y == board[x].length
        return false
    end
    if board[x][y] != word[i]
        return false
    end
    tmp = board[x][y]
    board[x][y] = "-"
    exist = existRec(board, x+1, y, word, i+1) ||
            existRec(board, x-1, y, word, i+1) ||
            existRec(board, x, y+1, word, i+1) ||
            existRec(board, x, y-1, word, i+1)
    board[x][y] = tmp
    return exist
end