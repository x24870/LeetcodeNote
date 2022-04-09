const gridTravel = (m, n, memo={}) => {
    if (m === 0 || n === 0) { return 0 };
    if (m === 1 || m === 1) { return 1 };

    let key = m + ',' + n;
    if (memo[key]){ return memo[key] };

    memo[key] = (gridTravel(m-1, n, memo) + gridTravel(m, n-1, memo));
    return memo[key]
}

console.log(gridTravel(2, 3)) //3
console.log(gridTravel(3, 2)) //3
console.log(gridTravel(3, 3)) //6
console.log(gridTravel(18, 18)) // 2333606220