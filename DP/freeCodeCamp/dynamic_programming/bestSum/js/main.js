const bestSum = (target, arr) => {
    if (target === 0) return [];
    if (target < 0) return null;

    let shortest = null;
    for(num of arr) { // for...of iterate value, for...in iterate index
        let reminder = target - num;
        let res = bestSum(reminder, arr);
        if (res !== null) {
            res = [...res, num];
            if (shortest == null || shortest.length > res.length) {
                shortest = res;
            }
        }
    }

    return shortest;
}

const bestSumMemo = (target, arr, memo={}) => {
    if (memo[target] !== undefined) return memo[target];
    if (target === 0) return [];
    if (target < 0) return null;

    let shortest = null
    for (num of arr) {
        let reminder = target - num;
        let res = bestSumMemo(reminder, arr, memo);
        if (res !== null) {
            res = [...res, num];
            if (shortest === null || shortest.length > res.length) {
                shortest = res;
            }
        }
    }

    memo[target] = shortest;
    return memo[target];
}

console.log(bestSum(7, [5,3,4,7])) // [4, 3]
console.log(bestSum(8, [2, 3, 5])) // [5, 3]
console.log(bestSum(7, [2, 4])) // null

console.log(bestSumMemo(7, [5,3,4,7])) // [4, 3]
console.log(bestSumMemo(8, [2, 3, 5])) // [5, 3]
console.log(bestSumMemo(7, [2, 4])) // null
console.log(bestSumMemo(100, [1, 2, 5, 25])) // [25, 25, 25, 25]