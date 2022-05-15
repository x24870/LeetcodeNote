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

const allConstructTable = (target, words) => {
    let table = Array(target.length + 1)
    .fill()
    .map(() => []);

    table[0] = [[]];

    for (let i=0; i<table.length; i++) {
        for (let w of words) {
            let start = i;
            let end = i + w.length;
            if (end < table.length && target.slice(start, end) === w) {
                for (let way of table[start]) {
                    let newWay = [...way, w];
                    table[end].push(newWay);
                }
            }
        }
    }

    return table[target.length];
}

console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
console.log(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
console.log("---")

console.log(allConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeez", 
[
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]))
console.log("---")

console.log(allConstructTable("purple", ["purp", "p", "ur", "le", "purpl"]))
console.log(allConstructTable("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
console.log(allConstructTable("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))