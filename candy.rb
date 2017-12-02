# @param {Integer[]} ratings
# @return {Integer}
def candy(ratings)
    size = ratings.length
    if size <= 1
        return size
    end
    num = Array.new(size, 1)
    (1...size).each do |i|
        if ratings[i] > ratings[i-1]
            num[i] = num[i-1] + 1
        end
    end
    (1...size).reverse_each do |i|
        if ratings[i-1] > ratings[i]
            num[i-1] = [num[i]+1, num[i-1]].max
        end
    end
    num.sum
end
