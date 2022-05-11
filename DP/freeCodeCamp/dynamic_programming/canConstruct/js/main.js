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


const canConstructTable = (target, words) => {
    let table = Array(target.length + 1).fill(false);
    table[0] = true;

    for (let idx=0; idx<table.length; idx++) {
        if (table[idx] === true) {
            for (let w of words) {
                let end = idx + w.length;
                if (w === target.slice(idx, end)) {
                    table[end] = true;
                }
            }
        }
    }

    return table[target.length]
}

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) // true
console.log(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) // false
console.log(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // true
console.log("---")

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
console.log("---")

console.log(canConstructTable("abcdef", ["ab", "abc", "cd", "def", "abcd"])) // true
console.log(canConstructTable("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) // false
console.log(canConstructTable("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // true
console.log(canConstructTable("eeeeeeeeeeeeeeeeeeeeeeeeeeef", 
[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
])) // false