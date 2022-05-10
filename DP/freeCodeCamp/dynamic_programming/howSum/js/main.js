// m = target, n = len(arr)
// time complexity: O(n^m)
// space complexity: O(m)
const howSum = (target, arr) => {
    if (target === 0) return []
    if (target < 0) return null

    for (let i=0; i<arr.length; i++){

        let reminder = target - arr[i]
        let how = howSum(reminder, arr)

        if (how !== null) {
            how.push(arr[i])
            return how
        }
    }

    return null
}

// modern syntax
// time complexity: O(n^m * m)
// space complexity: O(m)
const howSum2 = (target, arr) => {
    if (target === 0) return []
    if (target < 0) return null

    for (let num of arr) {
        let reminder = target - num;
        let how = howSum2(reminder, arr);

        if (how !== null){
            how = [...how, num]; // recreate an array, considering the wrost case that the length of the array equals to target
            return how
        }
    }

    return null
}

// time complexity: O(n*m * m)
// space complexity: O(m^2)
const howSumMemo = (target, arr, memo={}) => {
    if (memo[target] !== undefined) return memo[target]
    if (target === 0) return []
    if (target < 0) return null

    for (let i=0; i<arr.length; i++){

        let reminder = target - arr[i]
        let how = howSumMemo(reminder, arr, memo)

        if (how !== null) {
            memo[target] = [...how, arr[i]]
            return memo[target]
        }
    }

    memo[target] = null
    return memo[target]
}

const howSumTable = (target, arr) => {
    let table = Array(target+1).fill(null);
    table[0] = [];
    
    for (let i=0; i<=target; i++) {
        if (table[i] !== null) {
            for (let num of arr) {
                let sum = i + num;
                if (sum <= target) {
                    table[sum] = [num, ...table[i]];
                }
            }
        }
    }

    return table[target]
}

console.log(howSum(7, [5,3,4,7])) // [4, 3]
console.log(howSum(7, [2,4])) // null
console.log("---")

console.log(howSum2(7, [5,3,4,7])) // [4, 3]
console.log(howSum2(7, [2,4])) // null
console.log("---")

console.log(howSumMemo(300, [7, 14])) // null
console.log("---")

console.log(howSumTable(7, [5,3,4,7])) // [4, 3]
console.log(howSumTable(300, [7, 14])) // null