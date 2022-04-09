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


console.log(fibo(50))
