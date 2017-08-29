// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
//
// Example:
//
// Input: "babad"
//
// Output: "bab"
//
// Note: "aba" is also a valid answer.
//
//
//
// Example:
//
// Input: "cbbd"
//
// Output: "bb"
//


/**
 * @param {string} s
 * @return {string}
 */
var extendPalindrome = function(s, j, k) {
    // to find the longest palindrome, we dont search from the start point, 
    // but rather test if the current char is the mid point of a palindrom str.
    var str = '';
    var length = 0;
    while(j >= 0 && k < s.length && s.charAt(j) === s.charAt(k)) {
        j--;
        k++;
    }
    return {
        str: s.substring(j + 1, k), // because j-- and k++ above, we should undo those
        length: k - j - 1
    }
}

var longestPalindrome = function(s) {
    var longestStr = '';
    if (s.length < 2) return s;
    
    for (let i = 0; i < s.length - 1; i++) {
        // if the palindrome's length is odd
        var oddResult = extendPalindrome(s, i, i);
        // if even
        var evenResult = extendPalindrome(s, i, i + 1);
        
        // console.log(oddResult.str);
        // console.log(evenResult.str);
        if (oddResult.length > longestStr.length) longestStr = oddResult.str;
        if (evenResult.length > longestStr.length) longestStr = evenResult.str;
    }
    return longestStr;
};
