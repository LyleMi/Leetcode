# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    ret = Hash.new
    for s in strs
        ca = s.split(//).sort.join
        if not ret.has_key?(ca)
            ret[ca] = Array.new
        end
        ret[ca].push(s)
    end
    ret.values
end

puts group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])