const canConstruct = (target, words) => {
    if (target === "") return true;

    for (let w of words) {
        if (target.indexOf(w) === 0) {
            let subStr = target.slice(w.length);
            if (canConstruct(subStr, words) === true) {
                return true;
            }
        }
    }

    return false;
}

const canConstructMemo = (target, words, memo={}) => {
    if (memo[target] !== undefined) return memo[target];
    if (target === "") return true;

    for (let w of words) {
        if (target.indexOf(w) === 0) {
            let subStr = target.slice(w.length);
            if (canConstructMemo(subStr, words, memo) === true) {
                memo[target] = true;
                return true;
            }
        }
    }

    memo[target] = false;
    return false;
}


console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) // true
console.log(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) // false
console.log(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // true

console.log(canConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcd"])) // true
console.log(canConstructMemo("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) // false
console.log(canConstructMemo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // true
console.log(canConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeeef", 
[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
])) // false