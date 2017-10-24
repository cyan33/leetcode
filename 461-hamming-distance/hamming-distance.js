// The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
//
// Given two integers x and y, calculate the Hamming distance.
//
// Note:
// 0 &le; x, y &lt; 231.
//
//
// Example:
//
// Input: x = 1, y = 4
//
// Output: 2
//
// Explanation:
// 1   (0 0 0 1)
// 4   (0 1 0 0)
//        &uarr;   &uarr;
//
// The above arrows point to positions where the corresponding bits are different.
//


/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
//     let xBinStr = x.toString(2).split('').reverse().join('')
//     let yBinStr = y.toString(2).split('').reverse().join('')
    
//     let len = xBinStr.length > yBinStr.length ? xBinStr.length : yBinStr.length
//     let res = 0
    
//     for (let i = 0; i < len; i++) {
//         let currX = xBinStr[i] ? xBinStr[i] : '0'
//         let currY = yBinStr[i] ? yBinStr[i] : '0'
//         res = currX !== currY ? res + 1 : res
//     }
//     return res
    
    let xor = (x ^ y).toString(2).split('')
    return xor.reduce((accu, curr) => curr === '1' ? accu + 1 : accu, 0)
};
