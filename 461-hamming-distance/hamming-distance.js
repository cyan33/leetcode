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
 
var toBinary = function(x) {
    var binary = x.toString(2);
    while(binary.length < 31) {
        binary = "0" + binary;
    }
    
    return binary.split("");
};

var hammingDistance = function(x, y) {
    var xBinArr = toBinary(x),
        yBinArr = toBinary(y),
        count = 0;
    
    xBinArr.forEach(function(bit, i) {
        if(bit !== yBinArr[i])  count++
    })
    
    return count;
};
