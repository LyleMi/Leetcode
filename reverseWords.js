var reverseWords = function(str) {
    return str.split(' ').filter(s => s !== '').reverse().join(' ');
};