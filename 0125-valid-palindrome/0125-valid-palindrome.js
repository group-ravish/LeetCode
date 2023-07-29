/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const lower = s.toLowerCase();
    const alphanumeric = lower.replace(/[^a-z0-9]/g, '');
    const reverse = alphanumeric.split('').reverse().join('');
    return alphanumeric === reverse;
};