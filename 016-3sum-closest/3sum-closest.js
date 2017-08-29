// Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
//
//
//     For example, given array S = {-1 2 1 -4}, and target = 1.
//
//     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums = nums.sort((a, b) => a - b);
    let resultSum = nums[0] + nums[1] + nums[2];
    
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue;   // skip the same result
        
        let j = i + 1, k = nums.length - 1;
        while (j < k) {
            let currSum = nums[i] + nums[j] + nums[k];
            if (Math.abs(target - currSum) < Math.abs(target - resultSum)) {
                resultSum = currSum;
                if (currSum == target) return currSum;
            }
            (currSum > target) ? k-- : j++;
        }
    }
    return resultSum;
};
