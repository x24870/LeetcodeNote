const countConstruct = (target, words) => {
    if (target === '') return 1;

    let total = 0;
    for (let w of words) {
        if (target.indexOf(w) === 0){
            let subStr = target.slice(w.length);
            total += countConstruct(subStr, words);
        }
    }

    return total
}

const countConstructMemo = (target, words, memo={}) => {
    if (target in memo) return memo[target];
    if (target === '') return 1;

    let total = 0;
    for (let w of words) {
        if (target.indexOf(w) === 0){
            let subStr = target.slice(w.length);
            total += countConstructMemo(subStr, words, memo);
        }
    }

    memo[target] = total
    return total
}


console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) // 1
console.log(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) // 0
console.log(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // 4

console.log(countConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeee", 
[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
])) // 56058368