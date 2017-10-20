// https://leetcode.com/problems/wildcard-matching/discuss/
var isMatch = function(s, p) {
    let si = 0,
        pi = 0,
        match = 0,
        idx = -1;
    while (si < s.length) {
        if (pi < p.length && (p[pi] == "?" || s[si] == p[pi])) {
            si += 1;
            pi += 1;
        } else if (pi < p.length && p[pi] == "*") {
            idx = pi;
            match = si;
            pi += 1;
        } else if (idx != -1) {
            pi = idx + 1;
            match += 1;
            si = match;
        } else {
            return false;
        }
    }

    while (pi < p.length && p[pi] == "*") {
        pi += 1;
    }

    return pi === p.length;
};