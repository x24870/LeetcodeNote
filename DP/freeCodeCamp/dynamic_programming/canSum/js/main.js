// m = target
// n = len(arr)
// time complexity: O(n^m) (consider this: if there is 1 in arr, then this function has to minus 1 recursively till 0)
// space complexity: O(m)
const canSum = (target, arr) => {
    if (target === 0) return true;
    if (target < 0) return false;

    for (let i=0; i<arr.length; i++) {
        if(canSum(target - arr[i], arr) === true){
            return true
        }
    }

    return false
}


// time complexity: O(n*m)
// space complexity: O(m)
const canSumMemo = (target, arr, memo={}) => {
    if (target in memo) return memo[target];

    if (target === 0) return true;
    if (target < 0) return false;

    for (let i=0; i<arr.length; i++) {
        let reminder = target - arr[i];
        if (canSumMemo(reminder, arr, memo) === true){
            memo[target] = true
            return true
        }
    }

    memo[target] = false
    return false
}


console.log(canSum(7, [5,3,4,7])) // true
console.log(canSum(7, [2, 4])) // false
// console.log(canSum(300, [7, 14])) // too slow
console.log(canSumMemo(7, [5,3,4,7])) // true
console.log(canSumMemo(7, [2, 4])) // false
console.log(canSumMemo(300, [7, 14])) // false
console.log(canSumMemo(7000, [7, 14])) // true