# @param {String} num
# @return {Boolean}
def is_additive_number(num)
    n = num.length
    (1..n/2).each do |i|
        j = 1
        while [i, j].max <= n-i-j
            if is_valid(i, j, num)
                return true
            end
            j += 1
        end
    end
    false
end

def is_valid(i, j, num)
    if num[0] == '0' and i > 1
        return false
    end
    if num[i] == '0' and j > 1
        return false
    end
    x1 = num[0, i].to_i
    x2 = num[i, j].to_i
    start = i + j
    while start != num.length
        x2 += x1
        x1 = x2 - x1
        sum = x2.to_s
        if not num[start, num.length - start].start_with?(sum)
            return false
        end
        start += sum.length
    end
    return true
end

puts is_additive_number("112358")
puts is_additive_number("199100199")
