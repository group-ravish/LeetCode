/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    const first = {};
    const second = {};

    for (var i = 0; i < s.length; i++) {
        const char = s.charAt(i);
        if (first[char]) {
            first[char]++;
        } else {
            first[char] = 1;
        }
    }
    for (var i = 0; i < t.length; i++) {
        const char = t.charAt(i);
        if (second[char]) {
            second[char]++;
        } else {
            second[char] = 1;
        }
    }
    for (let char in first) {
        if (first[char] !== second[char]) {
            return false;
        }
    }
    return true;
};