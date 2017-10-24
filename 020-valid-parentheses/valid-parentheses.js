// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//
// The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


/**
 * @param {string} s
 * @return {boolean}
 */
// a valid one should be like: '({[]})'
// in the stack -> [')', '}', ']']
var isValid = function(s) {
    let res = []
    let charArr = s.split('')
    const dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    for (let p of charArr) {
        if (p === '(' || p === '{' || p === '[') {
            res.push(dict[p])
        } else {
            let curr = res.pop()
            if (p !== curr) return false
        }
    }
    return res.length === 0
};
