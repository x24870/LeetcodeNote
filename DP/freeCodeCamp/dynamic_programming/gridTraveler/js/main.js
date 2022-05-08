const gridTravel = (m, n, memo={}) => {
    if (m === 0 || n === 0) { return 0 };
    if (m === 1 || m === 1) { return 1 };

    let key = m + ',' + n;
    if (memo[key]){ return memo[key] };

    memo[key] = (gridTravel(m-1, n, memo) + gridTravel(m, n-1, memo));
    return memo[key]
}

const gridTravelTable = (m, n) => {
    // init a 2D array
    let table = Array(m+1)
    .fill()
    .map(() => Array(n+1).fill(0));

    // init starter grid
    table[1][1] = 1;

    for (i=0; i<=m; i++) {
        for (j=0; j<=n; j++) {
            const cur = table[i][j]
            if (j<n) table[i][j+1] += cur;
            if (i<m) table[i+1][j] += cur;
        }
    }

    return table[m][n]
}

console.log(gridTravel(2, 3)) //3
console.log(gridTravel(3, 2)) //3
console.log(gridTravel(3, 3)) //6
console.log(gridTravel(18, 18)) // 2333606220

console.log(gridTravelTable(2, 3)) //3
console.log(gridTravelTable(3, 2)) //3
console.log(gridTravelTable(3, 3)) //6
console.log(gridTravelTable(18, 18)) // 2333606220