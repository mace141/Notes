// [[[[[[[[[[[[[[[[[[[[[[[[[ #1 max value ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, maxValue, that takes in array of numbers as an argument. 
// The function should return the largest number in the array.
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

// ========================= Solution =========================
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

// [[[[[[[[[[[[[[[[[[[[[[[[[ #2 is prime ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, isPrime, that takes in a number as an argument. The function 
// should return a boolean indicating whether or not the given number is prime.
//
// A prime number is a number that is only divisible two distinct numbers: 1 and itself.
//
// For example, 7 is a prime because it is only divisible by 1 and 7. For example, 
// 6 is not a prime because it is divisible by 1, 2, 3, and 6.
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

// [[[[[[[[[[[[[[[[[[[[[[[[[ #3 uncompress ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, uncompress, that takes in a string as an argument. The input 
// string will be formatted into multiple groups according to the following pattern:
//
// <number><char>
//
// for example, '2c' or '3a'.
// The function should return an uncompressed version of the string where each 
// 'char' of a group is repeated 'number' times concecutively. You may assume that 
// the input string is well-formed according to the previously mentioned pattern.
//
// test_00:
// uncompress("2c3a1t"); // -> 'ccaaat'
// test_01:
// uncompress("4s2b"); // -> 'ssssbb'
// test_02:
// uncompress("2p1o5p"); // -> 'ppoppppp'
// test_03:
// uncompress("3n12e2z"); // -> 'nnneeeeeeeeeeeezz'

const uncompress = (s) => {
  // todo
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  let string = "";
  let numStr = "";

  for (let i = 0; i < s.length; i++) {
    if (!alphabet.includes(s[i])) {
      numStr += s[i];
    } else {
      for (let j = 0; j < parseInt(numStr); j++) {
        string += s[i];
      }
      numStr = "";
    }
  }

  return string;
};

// ========================= Solution =========================
// using two pointers
// const uncompress = (s) => {
//   let result = [];
//   const numbers = '0123456789';
//   let i = 0;
//   let j = 0;
//   while (j < s.length) {
//     if (numbers.includes(s[j])) {
//       j += 1;
//     } else {
//       const num = Number(s.slice(i, j));
//       for (let count = 0; count < num; count += 1) {
//         result.push(s[j]);
//       }
//       j += 1;
//       i = j;
//     }
//   }
//   return result.join('');
// };

// [[[[[[[[[[[[[[[[[[[[[[[[[ #4 compress ]]]]]]]]]]]]]]]]]]]]]]]]]
//
// Write a function, compress, that takes in a string as an argument. The function 
// should return a compressed version of the string where consecutive occurences
// of the same characters are compressed into the number of occurences followed 
// by the character. Single character occurences should not be changed.
//
// 'aaa' compresses to '3a'
// 'cc' compresses to '2c'
// 't' should remain as 't'
// You can assume that the input only contains alphabetic characters.
//
// test_00:
// compress('ccaaatsss'); // -> '2c3at3s'
// test_01:
// compress('ssssbbz'); // -> '4s2bz'
// test_02:
// compress('ppoppppp'); // -> '2po5p'
// test_03:
// compress('nnneeeeeeeeeeeezz'); // -> '3n12e2z'