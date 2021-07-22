// [[[[[[[[[[[[[[[[[[[[[[[[[ #1 max value ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, maxValue, that takes in array of numbers as an argument. The function should return the largest number in the array.
//
// Solve this without using any built-in array methods.
//
// You can assume that the array is non-empty.
//
// test_00:
// maxValue([4, 7, 2, 8, 10, 9]); // -> 10
// test_01:
// maxValue([10, 5, 40, 40.3]); // -> 40.3
// test_02:
// maxValue([-5, -2, -1, -11]); // -> -1
// test_03:
// maxValue([42]); // -> 42
// test_04:
// maxValue([1000, 8]); // -> 1000
// test_05:
// maxValue([1000, 8, 9000]); // -> 9000

const maxValue = (nums) => {
  // todo
  let i = 0;
  let max = nums[i];

  while (nums[i]) {
    if (nums[i] > max) {
      max = nums[i]
    }
    i++
  }
  
  return max;
};

// Solution 
//
// const maxValue = (nums) => {
//   let maximum = -Infinity;
//
//   for (let num of nums) {
//     if (num > maximum) maximum = num;
//   }
//
//   return maximum;
// };

// [[[[[[[[[[[[[[[[[[[[[[[[[ #1 is prime ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, isPrime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.
//
// A prime number is a number that is only divisible two distinct numbers: 1 and itself.
//
// For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.
//
// You can assume that the input number is a positive integer.
//
// test_00:
// isPrime(2); // -> true
// test_01:
// isPrime(3); // -> true
// test_02:
// isPrime(4); // -> false
// test_03:
// isPrime(5); // -> true
// test_04:
// isPrime(6); // -> false
// test_05:
// isPrime(7); // -> true
// test_06:
// isPrime(8); // -> false
// test_07:
// isPrime(25); // -> false
// test_08:
// isPrime(31); // -> true
// test_09:
// isPrime(2017); // -> true
// test_10:
// isPrime(2048); // -> false
// test_11:
// isPrime(1); // -> false

const isPrime = (n) => {
  // todo
  if (n < 2) return false;
  
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) return false;
  }
  
  return true;
};

