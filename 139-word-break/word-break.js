//
// Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
//
//
// For example, given
// s = "leetcode",
// dict = ["leet", "code"].
//
//
//
// Return true because "leetcode" can be segmented as "leet code".
//
//
//
// UPDATE (2017/1/4):
// The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let res = Array(s.length).fill(false)
    
    for (let i = 0; i < s.length; i++) {
        for (let word of wordDict) {
            if (word === s.slice(i - word.length + 1, i + 1) && (i - word.length === -1 || res[i - word.length])) {
                res[i] = true
            }   
        }
    }
    return res[res.length - 1]
};
