// Given a collection of intervals, merge all overlapping intervals.
//
//
// For example,
// Given [1,3],[2,6],[8,10],[15,18],
// return [1,6],[8,10],[15,18].


/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
    if (!intervals.length)  return []
    
    intervals.sort((a, b) => a.start - b.start)
    const res = [intervals[0]]
    
    for (let i = 1; i < intervals.length; i += 1) {
        if (intervals[i].start <= res[res.length - 1].end) {
            res[res.length - 1].end = Math.max(intervals[i].end, res[res.length - 1].end)
        } else {
            res.push(intervals[i])
        }
    }
    
    return res
};
