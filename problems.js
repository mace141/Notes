// Write a function, minChange(coins, amount), that accepts an array of coin values
// and a target amount as arguments. The method should the minimum number of coins needed
// to make the target amount. A coin value can be used multiple times.
//
// After you pass the first 3 examples, you'll likely need to memoize your code 
// in order to pass the 4th example in a decent runtime.
//
// Examples:
//  
// minChange([1, 2, 5], 11)         // => 3, because 5 + 5 + 1 = 11
// minChange([1, 4, 5], 8))         // => 2, because 4 + 4 = 8
// minChange([1, 5, 10, 25], 15)    // => 2, because 10 + 5 = 15
// minChange([1, 5, 10, 25], 100)   // => 4, because 25 + 25 + 25 + 25 = 100
function minChange(coins, amount, memo = {}) {
  if (amount == 0) return 0;
  if (memo[amount]) return memo[amount];

  const numCoins = [];
  coins.forEach(coin => {
    if (coin <= amount) {
      numCoins.push(minChange(coins, amount - coin, memo) + 1);
    }
  });

  memo[amount] = Math.min(...numCoins);
  return memo[amount];
}