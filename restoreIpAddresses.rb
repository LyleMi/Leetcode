def restore_ip_addresses(s)
    res = []
    len = s.length
    i = 1
    while i < 4 and i < len - 2 do
        j = 1
        while j < 4 and (i+j) < len - 1 do 
            k = 1
            while k < 4 and (i+j+k) < len do
                if is_vaild(s[0, i]) and is_vaild(s[i, j]) and is_vaild(s[i+j, k]) and is_vaild(s[i+j+k, len])
                    res.push(s[0, i] + "." + s[i, j] + "." + s[i+j, k] + "." + s[i+j+k, len])
                end
                k += 1
            end
            j += 1
        end
        i += 1
    end
    res
end

def is_vaild(s)
    if s.length > 3 or s.length == 0 or (s[0] == '0' and s.length > 1) or s.to_i > 255
        return false
    end
    return true
end

# puts restore_ip_addresses("25525511135")