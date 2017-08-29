// Determine whether an integer is a palindrome. Do this without extra space.
//
// click to show spoilers.
//
// Some hints:
//
// Could negative integers be palindromes? (ie, -1)
//
// If you are thinking of converting the integer to string, note the restriction of using extra space.
//
// You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
//
// There is a more generic way of solving this problem.
//


/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || (x !== 0 && x % 10 === 0)) return false;
    
    // compare the half of the integer
    let str = x.toString();
    let startIndex = 0;
    let endIndex = str.length - 1;
    
    while (startIndex !== endIndex && startIndex < endIndex) {
        if (str[startIndex] !== str[endIndex]) {
            return false;
        }
        startIndex++;
        endIndex--;
    }
    return true;
};
