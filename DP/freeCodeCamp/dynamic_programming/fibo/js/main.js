const fibo = (num, memo={}) => {
    if (memo[num]){
        return memo[num]
    }

    if (num < 2){
        return num;
    }

    memo[num] = fibo(num-1, memo) + fibo(num-2, memo);
    return memo[num]
}

const fiboTable = (num) => {
    const table = Array(num+1).fill(0);
    table[1] = 1;

    for (let i=0; i<=num; i++) {
        table[i+1] += table[i];
        table[i+2] += table[i];
    }

    return table[num]
}

console.log(fibo(50))
console.log(fiboTable(50))
