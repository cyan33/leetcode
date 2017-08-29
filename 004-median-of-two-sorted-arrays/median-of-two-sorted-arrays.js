// There are two sorted arrays nums1 and nums2 of size m and n respectively.
//
// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
//
// Example 1:
//
// nums1 = [1, 3]
// nums2 = [2]
//
// The median is 2.0
//
//
//
// Example 2:
//
// nums1 = [1, 2]
// nums2 = [3, 4]
//
// The median is (2 + 3)/2 = 2.5
//


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedian = function(arr) {
    if (arr.length % 2 === 0) {
        return (arr[arr.length/2-1] + arr[arr.length/2]) / 2;
    } else {
        return arr[parseInt(arr.length/2)];
    }
}

var findMedianSortedArrays = function(nums1, nums2) {
    let i = 0;
    let j = 0;
    let nums = [];
    while (i < nums1.length || j < nums2.length) {
        if (!nums1[i] || nums2[j] < nums1[i]) {
            nums.push(nums2[j]);
            j++;
        } else {
            nums.push(nums1[i]);
            i++;
        }
    }
    return findMedian(nums);
};
