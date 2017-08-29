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
    let charArr = s.split('');
    let stack = [];
    let c;
    for (let i = 0; i < charArr.length; i++) {
        c = charArr[i];
        if (charArr[i] === '(') {
            stack.push(')');
        } else if (c === '{') {
            stack.push('}');
        } else if (c === '[') {
            stack.push(']');
        } else if (stack.length === 0 || stack.pop() !== c) {
            return false;
        }
    }
    return stack.length === 0;
};
