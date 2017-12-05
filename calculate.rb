# @param {String} s
# @return {Integer}
def calculate(s)
    if s.length == 0
        return 0
    end
    sign = '+'
    stack = []
    num = 0
    isNum = lambda {|i| i.to_i.to_s == i}
    for i in 0...s.length
        if isNum.call s[i]
            num = num * 10 + s[i].to_i
        end
        if (not (isNum.call s[i]) and s[i]!=' ') or (i == s.length - 1)
            if sign == '-'
                stack.push(-num)
            elsif sign == '+'
                stack.push(num)
            elsif sign == '*'
                stack.push(stack.pop * num)
            elsif sign == "/"
                tmp = stack.pop
                if tmp < 0
                    stack.push(-(-tmp / num))
                else
                    stack.push(tmp/num)
                end
            end
            sign = s[i]
            num = 0
        end
    end
    return stack.sum
end

print calculate("3+2*2"), "\t", 7, "\n"
print calculate("3/2"), "\t", 1, "\n"
print calculate("3+5/2"), "\t", 5, "\n"
print calculate("14-3/2"), "\t", 13, "\n"