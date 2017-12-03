def compare_version(version1, version2)
    levels1 = version1.split(".")
    levels2 = version2.split(".")
    length = [levels1.length, levels2.length].max
    (0...length).each do |i|
        v1 = i < levels1.length ? levels1[i].to_i : 0
        v2 = i < levels2.length ? levels2[i].to_i : 0
        if v1 > v2
            return 1
        elsif v1 < v2
            return -1
        end
    end
    return 0
end

print compare_version("1", "0"), ",", 1, "\n"
print compare_version("1.2.3", "1.2.1.4"), ",", 1, "\n"
print compare_version("1.2", "1.2.1.4"), ",", -1, "\n"
print compare_version("1.2.1.4.0", "1.2.1.4"), ",", 0, "\n"