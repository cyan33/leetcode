// Given a digit string, return all possible letter combinations that the number could represent.
//
//
//
// A mapping of digit to letters (just like on the telephone buttons) is given below.
//
//
//
// Input:Digit string "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
//
//
//
// Note:
// Although the above answer is in lexicographical order, your answer could be in any order you want.


/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const dict = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
    if (!digits.length) return []
    
    let res = dict[digits[0]].split('')
    digits.split('').slice(1).forEach(d => {
        const len = res.length
        const originalRes = [...res]
        
        // expand the original result
        for (let j = 0; j < dict[parseInt(d)].length - 1; j++) {
            res = res.concat(originalRes)
        }
    
        // append the character
        res = res.map((s, k) => {
            return s + dict[parseInt(d)][parseInt(k / len)]
        })
    })

    return res
};

