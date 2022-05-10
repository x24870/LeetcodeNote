const bestSum = (target, arr) => {
    if (target === 0) return [];
    if (target < 0) return null;

    let shortest = null;
    for(let num of arr) { // for...of iterate value, for...in iterate index
        let reminder = target - num;
        let res = bestSum(reminder, arr);
        if (res !== null) {
            res = [...res, num];
            if (shortest === null || shortest.length > res.length) {
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
    for (let num of arr) {
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

const bestSumTable = (target, arr) => {
    let table = Array(target+1).fill(null);
    // init table[0] to empty array, which means we don't have to take any number to sum up the target 0 and the empty array also is the best way to sum up. 
    table[0] = [];

    for (let i=0; i<=target; i++) {
        if (table[i] !== null) {
            for (let num of arr) {
                let sum = i + num;
                if (sum > target) continue;

                let way = [num, ...table[i]]
                if (table[sum] === null || table[sum].length > way.length) {
                    table[sum] = way;
                }
            }
        }
    }

    return table[target]
}

console.log(bestSum(7, [5,3,4,7])) // [7]
console.log(bestSum(8, [2, 3, 5])) // [5, 3]
console.log(bestSum(7, [2, 4])) // null
console.log("---")

console.log(bestSumMemo(7, [5,3,4,7])) // [7]
console.log(bestSumMemo(8, [2, 3, 5])) // [5, 3]
console.log(bestSumMemo(7, [2, 4])) // null
console.log(bestSumMemo(100, [1, 2, 5, 25])) // [25, 25, 25, 25]
console.log("---")

console.log(bestSumTable(7, [5,3,4,7])) // [7]
console.log(bestSumTable(8, [2, 3, 5])) // [5, 3]
console.log(bestSumTable(7, [2, 4])) // null
console.log(bestSumTable(100, [1, 2, 5, 25])) // [25, 25, 25, 25]