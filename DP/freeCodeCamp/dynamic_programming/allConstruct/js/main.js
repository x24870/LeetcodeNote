const allConstruct = (target, words) => {
    if (target === '') return [[]];

    let total = [];
    for (let w of words) {
        if (target.indexOf(w) === 0) {
            let subStr = target.slice(w.length)
            let ways = allConstruct(subStr, words)
            for (let i=0; i<ways.length; i++) {
                ways[i] = [w, ...ways[i]];
            }
            total.push(...ways);
        }
    }

    return total;
}

const allConstructMemo = (target, words, memo={}) => {
    if (target in memo) return memo[target];
    if (target === '') return [[]];

    let total = [];
    for (let w of words) {
        if (target.indexOf(w) === 0) {
            let subStr = target.slice(w.length)
            let ways = allConstructMemo(subStr, words, memo)
            for (let i=0; i<ways.length; i++) {
                ways[i] = [w, ...ways[i]];
            }
            total.push(...ways);
        }
    }

    memo[target] = total;
    return total;
}

console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
console.log(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

console.log(allConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeez", 
[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))
